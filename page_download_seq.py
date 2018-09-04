'''
Download random images using a sequential program
'''
import urllib.request
import time
import os
import threading

hosts = ["http://www.ox.ac.uk", "https://www.cam.ac.uk",
         "http://www.canterbury.ac.nz", "http://www.lincoln.ac.nz",
         "http://www.unitec.ac.nz", "http://www.victoria.ac.nz",
         "http://www.nzherald.co.nz", "https://www.ucl.ac.uk",
         "http://www.aut.ac.nz", "http://www.massey.ac.nz"]

def get_page(url, fname):
    print("Getting page from", url)
    urllib.request.urlretrieve(url, fname) #Get image and save it in a file

def sequentialProg():
	t0 = time.time()
	for page in hosts:
		elements = os.path.split(page)
		univ = elements[1].split('.')
		univ = univ[1]
		fname_page = "pages//" + univ + ".html"
		get_page(page, fname_page)
	t1 = time.time()
	total_time = t1 - t0
	print("Execution time: {} seconds".format(total_time))

def threadedProg ():
	t0 = time.time()
	threads = []
	for page in hosts:
		elements = os.path.split(page)
		univ = elements[1].split('.')
		univ = univ[1]
		fnamePage = "pages//" + univ + ".html"
		myThread = threading.Thread(name = "gp" + univ, target = get_page, args = [page, fnamePage])
		threads.append(myThread)
		myThread.start()
	
	for t in threads:
		t.join()
		
	t1 = time.time()
	total_time = t1 - t0
	print("Execution time: {} seconds".format(total_time))

def main():
	print("Sequential Program:\n")
	sequentialProg()
	print("\nThreaded Program:\n")
	threadedProg()

if __name__ == "__main__":
    main()

	
