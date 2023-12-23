import random
import pandas as pd

# Global data
Hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jum'at"]
Kelas = ["7A", "7B", "7C", "7D", "7E", "7F", "7G", "7H", "7I", "7J", "8A", "8B", "8C", "8D", "8E", "8F", "8G", "8H", "8I", "8J", "9A", "9B", "9C", "9D", "9E", "9F", "9G", "9H", "9I", "9J"]
Jam = ["07:00 - 09:00", "09:00 - 11:00", "11:00 - 13:00", "13:30 - 15:30"]
Pelajaran = ["(PAI)", "(PKN)", "(B. Indonesia)", "(Matematika)", "(IPA)", "(IPS)", "(B. Inggris)", "(Seni)", "(Penjas)", "(Prakarya)"]
Guru = ["Tri Elis Setiyowati; S.Pd", "Yurisnawati; S.Pd.I", "Tribowo.N; A.Md", "Eva Widarsih; SE", "Maswarna; S.Pd.B.Ind", "Yusdalipa; S.Pd.Mat", "Said mukhlis; S.Pd", "Supriyanto; S.Si", "Fitri Ningsih; S.Pd.I", "Drs. Dewirman", "Zairani; S.Pd", "Ernita; S.Pd", "Dra. Indira", "Agustina; S.Pd.Ind", "Ermawati; S.Pd.I", "Luqman Hakim; S.Pd", "Tiaranita Dekriati; S.Pd", "Drs. Ismardi", "Dra. Asmah", "Vera Erli; S.Pd", "Susyamti; S.Pd", "Indra; S.Pd", "Erfiza Nugraha P; S.Pd", "Inna Kurniasih; S.Pd.I", "Winarmi; S.Pd.B", "Yoga Dwi Tanjung; S.Pd", "Vivy Aressa; M.Pd", "Dewi Suryanti; S.Pd", "Ahmad Posma; S.Pd", "Ifdal; S.Pd", "Ully Norprahatini; S.Pd", "Yuni Haryati Sisilia; S.Pd", "Ridwanto; S.Pd", "Ridhuansyah; S.Pd", "Riska Atmanegara; S.Pd", "Asep Wijaya; S.Pd", "Agus Susanto; S.Pd", "Rivaldi; S.Pd", "Dadang; S.Pd", "Sutarni; S.Pd"]

GuPel = [
          [Guru[0], Pelajaran[5]],[Guru[1], Pelajaran[7]],
          [Guru[2], Pelajaran[9]],[Guru[3], Pelajaran[5]],
          [Guru[4], Pelajaran[2]],[Guru[5], Pelajaran[3]],
          [Guru[6], Pelajaran[5]],[Guru[7], Pelajaran[4]],
          [Guru[8], Pelajaran[0]],[Guru[9], Pelajaran[3]],
          [Guru[10], Pelajaran[6]],[Guru[11], Pelajaran[1]],
          [Guru[12], Pelajaran[1]],[Guru[13], Pelajaran[2]],
          [Guru[14], Pelajaran[6]],[Guru[15], Pelajaran[4]],
          [Guru[16], Pelajaran[3]],[Guru[17], Pelajaran[8]],
          [Guru[18], Pelajaran[2]],[Guru[19], Pelajaran[6]],
          [Guru[20], Pelajaran[4]],[Guru[21], Pelajaran[2]],
          [Guru[22], Pelajaran[3]],[Guru[23], Pelajaran[0]],
          [Guru[24], Pelajaran[7]],[Guru[25], Pelajaran[8]],
          [Guru[26], Pelajaran[1]],[Guru[27], Pelajaran[1]],
          [Guru[28], Pelajaran[9]],[Guru[29], Pelajaran[5]],
          [Guru[30], Pelajaran[6]],[Guru[31], Pelajaran[4]],
          [Guru[32], Pelajaran[2]],[Guru[33], Pelajaran[8]],
          [Guru[34], Pelajaran[4]],[Guru[35], Pelajaran[4]],
          [Guru[36], Pelajaran[6]],[Guru[37], Pelajaran[0]],
          [Guru[38], Pelajaran[9]],[Guru[39], Pelajaran[3]]
        ]

# Find the best value (agar tidak ada guru yang sama di hari dan jam yang sama)
def fitness_(temp) :
    Idx = len(temp) + 1
    counter = 0
    for i in range(0,Idx) :
        for j in range(i+1,Idx-1) :
            if (temp[i][3] == temp[j][3]) and (temp[i][1] == temp[j][1]) and (temp[i][2] == temp[j][2]) :
              counter = counter + 1
    if counter == 0 :
      return 0
    else :
      return abs(1/counter)
    
# Mutation ideal for (So that no teacher teaches on the same day and time)
def mutation_ideal_(temp) :
  Idx = len(temp) + 1
  for i in range(0,Idx) :
    for j in range(i+1,Idx-1) :
      if (temp[i][3] == temp[j][3]) and (temp[i][1] == temp[j][1]) and (temp[i][2] == temp[j][2]) :          
        temp[i][3] = random.choice(GuPel)

# Find the best value (agar tidak ada guru yang sama(guru ngajar 2x) di hari dan kelas yang sama)
def constraints_(temp) :
  Idx = len(temp) + 1
  counts = 0
  for i in range(0,Idx) :
    for j in range(i+1,Idx-1) :
      if (temp[i][3] == temp[j][3]) and (temp[i][1] == temp[j][1]) and (temp[i][0] == temp[j][0]) :
        counts = counts + 1
  if counts == 0 :
    return 0
  else :
    return abs(1/counts)
  
# Mutation ideal for (So that no teacher teaches 2x in the same class and day)
def mutation_ideal_const_(temp) :
  IdxConst = len(temp) + 1
  for i in range(0,IdxConst) :
    for j in range(i+1,IdxConst-1) :
        if (temp[i][3] == temp[j][3]) and (temp[i][1] == temp[j][1]) and (temp[i][0] == temp[j][0]) :
          temp[i][3] = random.choice(GuPel)  

# Find the best value (agar tidak ada mata pelajaran yang sama namun gurunya berbeda dalam 1 kelas)
def constraints_teach_(temp) :
  Idx = len(temp) + 1
  counts = 0
  for i in range(0,Idx) :
    for j in range(i+1,Idx-1) :
      if (temp[i][3][0] != temp[j][3][0]) and (temp[i][0] == temp[j][0]) and (temp[i][3][1] == temp[j][3][1]) :
        counts = counts + 1
  if counts == 0 :
    return 0
  else :
    return abs(1/counts)

# Mutation ideal two (same with const_teach function)
def mutation_ideal_two_(temp) :
  Idx = len(temp) + 1
  for i in range(0,Idx) :
    for j in range(i+1,Idx-1) :
      if (temp[i][3][0] != temp[j][3][0]) and (temp[i][0] == temp[j][0]) and (temp[i][3][1] == temp[j][3][1]) :
        temp[j][3] = temp[i][3]
        
# Printout without table
def show_timetable_(temp) :
  countClass = 0
  for i in range(len(temp)) :
    if (countClass == 20) :
      countClass = 0
      print()
    if (countClass == 0) :
      print('{:21s}  ________'.format(''))
      print('{:21s} |Kelas {}|'.format('',str(temp[i][0])))
      print('{:21s}  --------'.format(''))
      print("================================================================")
      print('{:2s} ____ {:8s} ___ {:12s} ____________' .format('', '', ''))
      print('{:2s} Hari {:8s} Jam {:12s} Guru & Mapel' .format('', '', ''))
      print('{:2s} ____ {:8s} ___ {:12s} ____________' .format('', '', ''))
    print('|{:8s}| |{:12s}| |{:38s}|{:2s}' .format(temp[i][1], temp[i][2], temp[i][3], ''))
    countClass = countClass + 1

# Function of genetic_algorithm   
def genetic_algorithm_evo_(temp) :
  for i in range(10000) :
    new = []
    new.append([fitness_(temp), constraints_(temp), constraints_teach_(temp), temp])
    print("Gen {}, Fitness : {} Const : {} Teach : {}".format(i, fitness_(temp), constraints_(temp), constraints_teach_(temp)))
    addScheduleUpdate = []
    if (new[0][0] == 0 and new[0][1] == 0 and new[0][2] == 0) :
      break
    mutation_ideal_(temp)
    mutation_ideal_const_(temp)
    mutation_ideal_two_(temp)
    addScheduleUpdate = new
    temp = addScheduleUpdate[0][3]

# convert to txt file
def write_data_txt_(temp) :
  filepath = 'Jadwal'
  f = open('files/' + filepath, 'w')
  f.write('-----------------------SCHEDULE-----------------------\n')
  countClass = 0
  for i in range(len(temp)) :
    if (countClass == 20) :
      countClass = 0
      f.write('\n')
    if (countClass == 0) :
      f.write('{:21s}  ________\n'.format(''))
      f.write('{:21s} |Kelas {}|\n'.format('',str(temp[i][0])))
      f.write('{:21s}  --------\n'.format(''))
      f.write("================================================================\n")
      f.write('{:2s} ____ {:8s} ___ {:12s} ____________\n' .format('', '', ''))
      f.write('{:2s} Hari {:8s} Jam {:12s} Guru & Mapel\n' .format('', '', ''))
      f.write('{:2s} ____ {:8s} ___ {:12s} ____________\n' .format('', '', ''))
    f.write('|{:8s}| |{:12s}| |{:38s}|{:2s}\n' .format(temp[i][1], temp[i][2], temp[i][3], ''))
    countClass = countClass + 1
  f.close()

# Export to excel from data frame
def write_data_xlsx(temp) :
  column = ['Kelas', 'Hari', 'Jam', 'Guru & Mapel']
  df = pd.DataFrame(temp, columns=column)
  df.to_excel("files\Jadwal.xlsx", sheet_name='Schedule')

# Main Program
def main_() :
  # Input data
  temp = []
  for i in range(len(Kelas)) :
    for j in range(len(Hari)) :
      for x in range(len(Jam)) :
        temp.append([Kelas[i], Hari[j], Jam[x]])

  random.shuffle(GuPel)
  for i in range(len(temp)) :
    temp[i].append(random.choice(GuPel))

  # Function of genetic_algorithm
  genetic_algorithm_evo_(temp)

  # Remove string/char tidak perlu
  for i in range(len(temp)) :
    temp[i][3] = str(temp[i][3])[1:-1]
    temp[i][3] = str(temp[i][3]).replace("'", "").replace(",", "").replace(";", ",")

  # Printout without table
  show_timetable_(temp)

  # Export to excel from data frame
  # ==============================
  write_data_xlsx(temp)
  write_data_txt_(temp)
  print()
  print("JADWAL SELESAI DIBUAT")
 
# Run 
if __name__ == '__main__' :
  main_()
  
# NOTE :
# Ketika iterasi GEN melebihi 100 atau 120, maka restart ulang program