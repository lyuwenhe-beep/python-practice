file =open("poem.txt","w")
file.write("高处不胜寒,\n起舞弄清影，\n何似在人间")
file.close()

file =open("poem.txt","a")
file.write("\n但愿人长久，\n千里共婵娟")
file.close()
