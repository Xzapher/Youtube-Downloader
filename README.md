# Youtube-Downloader
Youtube Downloader made in python using pytube and tkinter /.exe

Actually this app is so simple, a big console/cmd showing you what is happening and 3 buttons and a box field to paste an url:

Select dir: choose where do you want to export the final video

download video/audio: necessary to explain?

maybe my code it is not the cleanest you ever seen, i did it to work in any situation that you miss some files or the path.txt

       ⣠⣶⣿⣿⢳⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣶⣭⣻⢿⢯⣞⡝⣿⣿⣫⢃⣛⣵⣾⣿        ⢀⣾
      ⣰⣿⣿⣿⣏⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⡿⣟⣯⣷⣾⢸⣿⣿⣿⣷⣿⡏⠁⣿⣿⡀⢸⣿⣿⣿⣿        ⣼⣿
     ⣼⣿⣿⣿⡟⣼⣿⣿⡇⣿⣿⣿⣿⡿⣟⣽⣾⣿⣿⣿⣿⡏⣿⣿⣿⣿⣿⣷⡴⠿⢟⣛⣭⣭⣭⣭⣝⣀      ⢠⣿⣿⡀
    ⣸⣿⣿⣿⣿⢱⣿⣿⣿⡇⣿⣿⡿⣫⣾⣿⣿⡿⣻⣵⣶⣿⣿⣷⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀   ⢸⣿⣿⡇
   ⢰⣿⣿⣿⣿⡟⣾⣿⣿⣿⣧⠹⣫⣾⣿⣿⣿⣫⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆  ⢸⣿⣿⣿
   ⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣎⢿⣿⣿⣿⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆ ⢸⣿⣿⣿⡇
  ⢸⣿⣿⣿⣿⣿⢹⣿⣿⣿⣿⣿⣿⣦⡻⣿⢧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢹⣿⣿⣿⣿⣿⣿⣿⣿⣇⢿⣿⣿⣿⣿
  ⣾⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⡆⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⠿⣿⡎⣿⣿⣿⣿⡇
  ⣿⣿⣿⣿⣿⣿⡜⣿⣿⣿⣿⣿⣿⣿⡿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⢻⣿⣿⣿⡿⠛⣡⣾⣿⣿⡜⣿⣿⣿⣇
 ⢸⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⢟⣵⣟⣼⣿⣟⠻⣿⣿⣿⣿⣿⣿⣿⢁⢿⣿⣿⣿⣿⣿⣿⣿⡿⣼⣎⢿⠿⢋⣴⣿⣿⣿⣿⣿⣷⡹⣿⣿⣿
 ⢸⣿⣿⣿⣿⣿⣿⣧⢻⣿⣿⣿⣟⣑⣚⢍⣾⣿⣿⣿⣷⣦⣙⠻⣿⣿⣿⢧⣿⡸⣿⣿⣿⣿⣿⣿⣿⢇⣿⠟⣀⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣜⠿⡟
 ⢸⣿⣿⣿⣿⣿⣿⣿⡘⣿⣿⣿⡿⢟⣵⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡙⠣⣿⣿⣧⢻⣿⣿⣿⣿⣿⠏⠜⡡⠞⠛⠃⠙⠿⠿⣿⣿⣿⢿⣿⣿⠿⣫⠇
 ⠈⣿⣿⣿⣿⣿⣿⡟⣷⢜⣫⣽⢞⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⠟⠵⠷⢬⡙⢿⡜⣿⢹⣿⣿⢏⣴⠊⣠⠶⠿⢷⣦⣄⠈⢙⣛⡛⣃⣐⣶⣾⠏
  ⣿⣿⣿⣿⣿⣿⣧⣿⣿⣔⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠂⣠⡤⠴⠦⢤⣙⣿⣧⠛⣼⠟⣡⣾⣿⣾⣿⡗  ⠹⣿⣆⠈⣙⡇⣿⣿⡿⠋ 
  .⢸⣿⣿⣿⣿⣿⣿⢉⣾⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠃⢠⣾⣿⡷   ⠻⣿⣿⣴⣷⣿⣿⣿⣿⡇⠉ ✨ ⢻⣿⡆⢿⣇⠛⠉ 
  .⠘⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣶⣤⣲⣶⣾⠿⢀⣿⣿⠙⠁✨ ⡀⢻⣿⣿⣿⣿⣿⣿⣿⣧⠰⣄⣀⣠⡇⢸⣿⣧⢺⣿⡄
   ⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⡇⢸⣿⣷⠠⣄⡀⢀⣰⡇⣸⣿⣿⣿⣿⣿⣿⣿⣿⣦⡙⠿⠿⣡⣿⢿⣿⡏⣿⣷⡀
   ⢻⣿⣿⣿⣿⣿⣿⣹⣿⣿⣿⣿⢏⣽⢸⣿⣿⣧⠘⣿⣿⣆⠙⠿⠿⢟⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⢲⢮⡿⣽⣷⣿⣿⣷
   ⣸⣿⣿⣿⣿⣿⣿⣧⢿⣿⣿⡏⣾⣯⡍⣿⣿⣿⡼⣯⣟⣛⣻⢶⢼⣟⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⣿⣿⠿⣫⣏⣾⢳⢳⢇⣿⣿⡿⡇
   ⣿⣟⣿⣿⣿⣿⣿⣿⣎⢿⣿⡇⣿⡿⡇⢻⣿⣿⣷⣝⠳⠷⢯⢏⣟⣾⡏⣙⣛⢛⣋⣥⣶⣶⣦⣄⡀⠐⠆⣿⣿⣿⣟⣫⢾⣿⣿⡇⠃
  ⡸⠋⣼⣿⣿⣿⣿⣿⣿⣿⣯⢿⣿⡜⠋⢀⡌⣿⣿⣿⣮⡩⢾⣯⣾⣿⣿⡇⣧⣣⣾⣿⣿⣿⣿⣿⣿⣿⣦ ⣿⣿⣿⣿⢏⣿⣿⠟⠁
   ⣸⣿⣿⣿⣿⣿⣿⣿⣿⢟⣽⣿⠃ ⣾⣿⡘⢿⣿⣿⣿⣷⡮⣹⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢱⣿⣿⣿⣋⠚⣩⡵⣸
  ⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⢦⣇ ⣿⣿⣿⣤⠓⠈⢽⣭⣾⣿⣿⣿⣷⡘⣿⣿⣿⣿⣿⣿⣿⣿⠟⣡⣿⣿⡿⢛⡁⠘⢛⣱⡇
  ⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡱⢿⣿⣦⡘⠿⠿⢟⣱⣶⣤⣽⡻⢿⣿⣿⣿⣿⣮⣙⠻⠿⠿⠟⣋⣡⣾⠿⢛⣥⣶⣿⣧⡀ ⠛
 ⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣶⣻⣿⣿⡏⠛⠿⡟⣫⠁⠸⢭⣝⣛⣛⣛⠿⡟⠛⢋⣭⣥⣶⣾⡟⠛⠋⢉⣁.
