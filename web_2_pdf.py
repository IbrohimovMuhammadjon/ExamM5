import pdfkit
from time import perf_counter
from multiprocessing import Process

path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

base_url = "https://tilshunos.com/omonims/?page="

def generate_pdf(i):
    pdfkit.from_url(base_url + str(i), 
                    "Omonimlar/" + str(i) + ".pdf", configuration=config)
    print(f"{i}-webpage saqlandi")

if __name__ == '__main__':
    start = perf_counter()
    process = []
    for i in range(1, 11): 
        p = Process(target=generate_pdf, args=(i,))
        process.append(p)
        p.start()

    for p in process:
        p.join()
    finish = perf_counter()

    print(f"{finish - start:.5f} seconds")
