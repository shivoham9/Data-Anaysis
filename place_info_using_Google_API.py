import json
import requests
import matplotlib.pyplot as plt
def get_place_info(place_name):
    key = "AIzaSyAtzvDoPkWFu8g6urdrhaManQq-zccP9RM"
    url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?inputtype=textquery&fields=photos,formatted_address,name,rating,place_id&input={place_name}&key={key}"
    page = requests.get(url)
    if page.status_code == 200:
        data = json.loads(page.text)
        if data['status'] == 'OK':
            for info in data['candidates']:
                print("_"*80, end='\n\n\n')
                name = info['name']
                address = info['formatted_address']
                place_id = info['place_id']
                print("Name: ", name)
                print("Address: ", address)
                for num,ph in enumerate(info['photos']):
                    ph_ref = ph['photo_reference']
                    url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={ph_ref}&key={key}"
                    page = requests.get(url)
                    if page.status_code == 200:
                        fp = open('myimg.jpg', 'wb')
                        fp.write(page.content)
                        fp.close()
                        im = plt.imread('myimg.jpg')
                        fig = plt.figure(figsize=(12,6))
                        ax = fig.add_axes([0, 0, 1, 1])
                        for sp in ax.spines:
                            ax.spines[sp].set_visble=False
                        ax.set_xticks([])
                        ax.set_yticks([])
                        plt.imshow(im)
                        plt.show()
                    else:
                        print("Invalid Response for Photo ", page.status_code)
                    
                    break

                print("_"*80, end='\n\n\n')


        else:
            print("No address found or something Wrong")
    else:
        print("Invalid Response from server as ", page.status_code)
        
if __name__ == "__main__":
    place = input("Enter palace name: ")
    get_place_info(place)
