from pytube import YouTube
def download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
    youtubeObject.download()
  except:
      print("there has been an error in downloading your youtube video")
      print(" WooHoo All Done!!")
link = input("Pick a Youtube link and place it here - URL: ")
download(link)


    
      
      
  