import csv
import glob

testArray = ['2013-04-13.csv', '2013-04-133.csv']
def combine(fileArray, savefile):
    nameArray = []
    dateArray = []
    openArray = []
    closeArray = []
    highArray = []
    lowArray = []
    volumeArray = []
    v0 = []
    v1 = []
    v2 = []
    v3 = []
    h0 = []
    h1 = []
    h2 = []
    h3 = []
    k0 = []
    k1 = []
    k2 = []
    k3 = []
    count=0
    with open(savefile, 'w', newline='') as newfile:
        newwriter = csv.writer(newfile)
        newwriter.writerow(["filename", "date", "open", "close", "high", "low", "volume", "Signal", "intensity"])
        for amount in range(len(fileArray)):
            r = csv.reader(open(fileArray[amount]))
            file = list(r)

            for paper in range(1, len(file)):
                if len(file[paper]) > 0:
                    bool = 0
                    for existingpaper in range(len(nameArray)):
                        if file[paper][0] == nameArray[existingpaper]:
                            bool = 1
                            if file[paper][7] == 'V0':
                                v0[existingpaper] = v0[existingpaper] + 1
                            if file[paper][7] == 'V1':
                                v1[existingpaper] = v1[existingpaper] + 1
                            if file[paper][7] == 'V2':
                                v2[existingpaper] = v2[existingpaper] + 1
                            if file[paper][7] == 'V3':
                                v3[existingpaper] = v3[existingpaper] + 1
                            if file[paper][7] == 'K0':
                                k0[existingpaper] = k0[existingpaper] + 1
                            if file[paper][7] == 'K1':
                                k1[existingpaper] = k1[existingpaper] + 1
                            if file[paper][7] == 'K2':
                                k2[existingpaper] = k2[existingpaper] + 1
                            if file[paper][7] == 'K3':
                                k3[existingpaper] = k3[existingpaper] + 1
                            if file[paper][7] == 'H0':
                                h0[existingpaper] = h0[existingpaper] + 1
                            if file[paper][7] == 'H1':
                                h1[existingpaper] = h1[existingpaper] + 1
                            if file[paper][7] == 'H2':
                                h2[existingpaper] = h2[existingpaper] + 1
                            if file[paper][7] == 'H3':
                                h3[existingpaper] = h3[existingpaper] + 1
                    if bool == 0:
                        nameArray.append(file[paper][0])
                        dateArray.append(file[paper][1])
                        openArray.append(file[paper][2])
                        closeArray.append(file[paper][3])
                        highArray.append(file[paper][4])
                        lowArray.append(file[paper][5])
                        volumeArray.append(file[paper][6])
                        if file[paper][7] == 'VO':
                            v0.append(1)
                        else:
                            v0.append(0)
                        if file[paper][7] == 'V1':
                            v1.append(1)
                        else:
                            v1.append(0)
                        if file[paper][7] == 'V2':
                            v2.append(1)
                        else:
                            v2.append(0)
                        if file[paper][7] == 'V3':
                            v3.append(1)
                        else:
                            v3.append(0)
                        if file[paper][7] == 'KO':
                            k0.append(1)
                        else:
                            k0.append(0)
                        if file[paper][7] == 'K1':
                            k1.append(1)
                        else:
                            k1.append(0)
                        if file[paper][7] == 'K2':
                            k2.append(1)
                        else:
                            k2.append(0)
                        if file[paper][7] == 'K3':
                            k3.append(1)
                        else:
                            k3.append(0)
                        if file[paper][7] == 'HO':
                            h0.append(1)
                        else:
                            h0.append(0)
                        if file[paper][7] == 'H1':
                            h1.append(1)
                        else:
                            h1.append(0)
                        if file[paper][7] == 'H2':
                            h2.append(1)
                        else:
                            h2.append(0)
                        if file[paper][7] == 'H3':
                            h3.append(1)
                        else:
                            h3.append(0)

        print(nameArray)
        print(dateArray)
        print(openArray)
        print(closeArray)
        print(v0)
        print(v1)
        print(k0)
        print(k1)
        print(h0)
        print(h1)
        for papers in range(len(nameArray)):
            h = 0
            k = 0
            v = 0
            h = h0[papers] + h1[papers] + h2[papers] + h3[papers]
            k = k0[papers] + k1[papers] + k2[papers] + k3[papers]
            v = v0[papers] + v1[papers] + v2[papers] + v3[papers]
            result = ''
            if v > k and v > h:
                signal = 'V'
                if v0[papers] > v1[papers] and v0[papers] > v2[papers] and v0[papers] > v3[papers]:
                    result = result + str(0)
                elif v1[papers] > v0[papers] and v1[papers] > v2[papers] and v1[papers] > v3[papers]:
                    result = result + str(1)
                elif v2[papers] > v0[papers] and v2[papers] > v1[papers] and v2[papers] > v3[papers]:
                    result = result + str(2)
                elif v3[papers] > v0[papers] and v3[papers] > v1[papers] and v3[papers] > v2[papers]:
                    result = result + str(3)
                elif v3[papers] + v2[papers] > v1[papers] + v0[papers]:
                    result = result + str(2)
                else:
                    result = result + str(0)

            elif k > v and k > h:
                signal = 'K'
                if k0[papers] > k1[papers] and k0[papers] > k2[papers] and k0[papers] > k3[papers]:
                    result = result + str(0)
                elif k1[papers] > k0[papers] and k1[papers] > k2[papers] and k1[papers] > k3[papers]:
                    result = result + str(1)
                elif k2[papers] > k0[papers] and k2[papers] > k1[papers] and k2[papers] > k3[papers]:
                    result = result + str(2)
                elif k3[papers] > k0[papers] and k3[papers] > k1[papers] and k3[papers] > k2[papers]:
                    result = result + str(3)
                elif k3[papers] + k2[papers] > k1[papers] + k0[papers]:
                    result = result + str(2)
                else:
                    result = result + str(0)
            else:
                signal = 'H'
                if h0[papers] > h1[papers] and h0[papers] > h2[papers] and h0[papers] > h3[papers]:
                    result = result + str(0)
                elif h1[papers] > h0[papers] and h1[papers] > h2[papers] and h1[papers] > h3[papers]:
                    result = result + str(1)
                elif h2[papers] > h0[papers] and h2[papers] > h1[papers] and h2[papers] > h3[papers]:
                    result = result + str(2)
                elif h3[papers] > h0[papers] and h3[papers] > h1[papers] and h3[papers] > h2[papers]:
                    result = result + str(3)
                elif h3[papers] + h2[papers] > h1[papers] + h0[papers]:
                    result = result + str(2)
                else:
                    result = result + str(0)
            newwriter.writerow([nameArray[papers], dateArray[papers], openArray[papers], closeArray[papers], highArray[papers], lowArray[papers], volumeArray[papers], signal,  result])
            print(result)
combine(testArray, 'output.csv')