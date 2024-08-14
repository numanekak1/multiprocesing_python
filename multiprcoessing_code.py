import multiprocessing
import requests

def downloadFile(url,name):
  print(F'Start Downloading")
  response=requests.get(url)

  open(F"image_{name}.jpg","wb").write(response.content)
  print(F'Downloading Finish')


  url="https://picsum.photos/2000/3000"
  pros=[]
  for i in range(100):
    p=multiprocessing.Process(target=downloadFile,args=[urls,i])
    p.start()
    pros.append(d)

for p in pros:
  p.join()
