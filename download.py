import os
import requests


def download_scan(deb, end, nb_chapitres):
    for chap_id in range(deb, end + 1):

        cmd = "mkdir " + str(chap_id)
        os.system(cmd)

        progression = round(((chap_id - deb) / (end - deb)) * 100, 2)
        print(str(progression) + "%")

        for id in range(0, nb_chapitres + 1):
            if id < 10:
                name = "0" + str(id)
            else:
                name = str(id)
            path_creator(chap_id, name)


def path_creator(chap_id, name):
    web_path = "https://lelscans.net/mangas/my-hero-academia/" + str(chap_id) + "/" + name + ".jpg"
    file_name = web_path.split('/')[-1]
    save_path = str(chap_id) + "/" + file_name
    download_png(web_path, save_path)


def download_png(web_path, save_path):
    img_data = requests.get(web_path, allow_redirects=True)
    if img_data.__str__() != "<Response [404]>":
        open(save_path, 'wb').write(img_data.content)


download_scan(190, 306, 22)

'''
pdf = FPDF()
pdf.set_auto_page_break(0)
imagelist = [i for i in os.listdir('Images') if i.endswith('jpg')]
pour l'image triée (imagelist):
pdf.add_page ()
pdf.image ('Images /' + image, w = 945, h = 1300)
'''
