def getTransactions(arrayNames, arrayState,amountToBuy):
    retArray=[]
    count=0
    v2Array = []
    v1Array=[]
    v0Array = []
    h2Array=[]
    h1Array = []
    h0Array = []
    k3Array = []
    k2Array = []
    k1Array = []
    k0Array = []
    buys=amountToBuy
    for elements in arrayState:
        print(count)
        #V3 state 7777 Sell it completly
        if arrayState[count] == "V3":
            retArray.append([arrayNames[count],"V", "100"])
        if arrayState[count] == "V2":
            v2Array.append(count)
        if arrayState[count] == "V1":
            v1Array.append(count)
        if arrayState[count] == "V0":
            v0Array.append(count)
        if arrayState[count] == "H2":
            h2Array.append(count)
        if arrayState[count] == "H1":
            h1Array.append(count)
        if arrayState[count] == "H0":
            h0Array.append(count)
        if arrayState[count] == "K3":
            k3Array.append(count)
        if arrayState[count] == "K2":
            k2Array.append(count)
        if arrayState[count] == "K1":
            k1Array.append(count)
        if arrayState[count] == "K0":
            k0Array.append(count)
        print(arrayState[count])
        count = count + 1
    if len(k3Array) >0:
        #sellpaers 77777777777777777777
        if len(v2Array)>0:
            for papers in v2Array:
                retArray.append([arrayNames[papers], "V", "100"])
        if len(v1Array)>0:
            for papers in v1Array:
                retArray.append([arrayNames[papers], "V", "100"])
        if len(v0Array)>0:
            for papers in v0Array:
                retArray.append([arrayNames[papers], "V", "100"])
        if len(h0Array)>0:
            for papers in h0Array:
                retArray.append([arrayNames[papers], "V", "50"])
        if len(h1Array)>0:
            for papers in h1Array:
                retArray.append([arrayNames[papers], "V", "25"])

        #buypapers 7777
        if len(k3Array) >= buys:
            divider = buys
            for papers in k3Array:
                if buys > 0:
                    retArray.append([arrayNames[papers], "K", str(100 / divider)])
                    buys = buys-1
        elif len(k3Array) >= buys/2:
            divider = len(k3Array)
            for papers in k3Array:
                retArray.append([arrayNames[papers], "K",  str(85 / divider)])
                buys = buys - 1

            if len(k2Array) > 0:
                if len(k2Array) >= buys:
                    divider = buys
                    for papers in k2Array:
                        if buys > 0:
                            retArray.append([arrayNames[papers], "K",  str(15 / divider)])
                            buys = buys - 1
                elif len(k2Array) >= buys / 2:
                    divider = len(k2Array)
                    for papers in k2Array:
                        retArray.append([arrayNames[papers], "K",  str(10 / divider)])
                        buys = buys - 1

                    if len(k1Array) > 0:
                        if len(k1Array) >= buys:
                            divider = buys
                            for papers in k1Array:
                                if buys > 0:
                                    retArray.append([arrayNames[papers], "K",  str(5 / divider)])
                                    buys = buys - 1
                        else:
                            divider = len(k1Array)
                            for papers in k1Array:
                                retArray.append([arrayNames[papers], "K", str(3.5 / divider)])
                                buys = buys - 1
                            if len(k0Array) > 0:
                                if len(k0Array) > buys:
                                    divider = buys
                                else:
                                    divider = len(k0Array)
                                for papers in k0Array:
                                    if buys > 0:
                                        retArray.append([arrayNames[papers], "K", str(1.5 / divider)])
                                        buys = buys - 1
                    else:
                        if len(k0Array) > 0:
                            if len(k0Array) > buys:
                                divider = buys
                            else:
                                divider = len(k0Array)
                            for papers in k0Array:
                                if buys > 0:
                                    retArray.append([arrayNames[papers], "K", str(3.5 / divider)])
                                    buys = buys - 1

                                    #extend evt 7777
                else:
                    divider = len(k2Array)
                    for papers in k2Array:
                        retArray.append([arrayNames[papers], "K", str(5 / divider)])
                        buys = buys - 1

                    if len(k1Array)>0:
                        if len(k1Array) >= buys:
                            divider = buys
                            for papers in k1Array:
                                if buys > 0:
                                    retArray.append([arrayNames[papers], "K", str(2 / divider)])
                                    buys = buys - 1

                        else:
                            divider = len(k1Array)
                            for papers in k1Array:
                                retArray.append([arrayNames[papers], "K", str(1 / divider)])
                                buys = buys - 1
                            if len(k0Array) > 0:
                                if len(k0Array) > buys:
                                    divider = buys
                                else:
                                    divider = len(k0Array)
                                for papers in k0Array:
                                    if buys > 0:
                                        retArray.append([arrayNames[papers], "K", str(0.5 / divider)])
                                        buys = buys - 1
            else:
                if len(k1Array) > 0:
                    if len(k1Array) >= buys:
                        divider = buys
                        for papers in k1Array:
                            if buys > 0:
                                retArray.append([arrayNames[papers], "K", str(4 / divider)])
                                buys = buys - 1
                    else:
                        divider = len(k1Array)
                        for papers in k1Array:
                            retArray.append([arrayNames[papers], "K", str(2 / divider)])
                            buys = buys - 1
                        if len(k0Array) >= buys:
                            divider = buys
                            for papers in k0Array:
                                if buys > 0:
                                    retArray.append([arrayNames[papers], "K", str(1 / divider)])
                                    buys = buys - 1
                        else:
                            divider = len(k0Array)
                            for papers in k0Array:
                                if buys > 0:
                                    retArray.append([arrayNames[papers], "K", str(0.5 / divider)])
                                    buys = buys - 1

                else:
                    if len(k0Array) > 0:
                        if len(k0Array) > buys:
                            divider = buys
                        else:
                            divider = len(k0Array)
                        for papers in k0Array:
                            if buys > 0:
                                retArray.append([arrayNames[papers], "K", str(3 / divider)])
                                buys = buys - 1

        elif len(k3Array) >= buys / 4:
            divider = len(k3Array)
            for papers in k3Array:
                retArray.append([arrayNames[papers], "K", str(60 / divider)])
                buys = buys - 1

            if len(k2Array) > 0:
                if len(k2Array) >= buys:
                    divider = buys
                    for papers in k2Array:
                        if buys > 0:
                            retArray.append([arrayNames[papers], "K", str(40 / divider)])
                            buys = buys - 1
                elif len(k2Array) >= buys / 2:
                    divider = len(k2Array)
                    for papers in k2Array:
                        retArray.append([arrayNames[papers], "K", str(25 / divider)])
                        buys = buys - 1

                    if len(k1Array) > 0:
                        if len(k1Array) >= buys:
                            divider = buys
                            for papers in k1Array:
                                if buys > 0:
                                    retArray.append([arrayNames[papers], "K", str(15 / divider)])
                                    buys = buys - 1
                        else:
                            divider = len(k1Array)
                            for papers in k1Array:
                                retArray.append([arrayNames[papers], "K", str(10 / divider)])
                                buys = buys - 1
                            if len(k0Array) > 0:
                                if len(k0Array) > buys:
                                    divider = buys
                                else:
                                    divider = len(k0Array)
                                for papers in k0Array:
                                    if buys > 0:
                                        retArray.append([arrayNames[papers], "K", str(5 / divider)])
                                        buys = buys - 1
                    else:
                        if len(k0Array) > 0:
                            if len(k0Array) > buys:
                                divider = buys
                            else:
                                divider = len(k0Array)
                            for papers in k0Array:
                                if buys > 0:
                                    retArray.append([arrayNames[papers], "K", str(7.5 / divider)])
                                    buys = buys - 1

                                    # extend evt 7777
                else:
                    divider = len(k2Array)
                    for papers in k2Array:
                        retArray.append([arrayNames[papers], "K", str(15 / divider)])
                        buys = buys - 1

                    if len(k1Array) > 0:
                        if len(k1Array) >= buys:
                            divider = buys
                            for papers in k1Array:
                                if buys > 0:
                                    retArray.append([arrayNames[papers], "K", str(10 / divider)])
                                    buys = buys - 1

                        else:
                            divider = len(k1Array)
                            for papers in k1Array:
                                retArray.append([arrayNames[papers], "K", str(5 / divider)])
                                buys = buys - 1
                            if len(k0Array) > 0:
                                if len(k0Array) > buys:
                                    divider = buys
                                else:
                                    divider = len(k0Array)
                                for papers in k0Array:
                                    if buys > 0:
                                        retArray.append([arrayNames[papers], "K", str(2.5 / divider)])
                                        buys = buys - 1
            else:
                if len(k1Array) > 0:
                    if len(k1Array) >= buys:
                        divider = buys
                        for papers in k1Array:
                            if buys > 0:
                                retArray.append([arrayNames[papers], "K", str(10 / divider)])
                                buys = buys - 1
                    else:
                        divider = len(k1Array)
                        for papers in k1Array:
                            retArray.append([arrayNames[papers], "K", str(7.5 / divider)])
                            buys = buys - 1
                        if len(k0Array) > 0:
                            if len(k0Array) >= buys:
                                divider = buys
                                for papers in k0Array:
                                    if buys > 0:
                                        retArray.append([arrayNames[papers], "K", str(5 / divider)])
                                        buys = buys - 1
                            else:
                                divider = len(k0Array)
                                for papers in k0Array:
                                    if buys > 0:
                                        retArray.append([arrayNames[papers], "K", str(3.5 / divider)])
                                        buys = buys - 1
                else:
                    if len(k0Array) > 0:
                        if len(k0Array) > buys:
                            divider = buys
                        else:
                            divider = len(k0Array)
                        for papers in k0Array:
                            if buys > 0:
                                retArray.append([arrayNames[papers], "K", str(4 / divider)])
                                buys = buys - 1



        else:
            divider = len(k3Array)
            for papers in k3Array:
                retArray.append([arrayNames[papers], "K", str(25 / divider)])
                buys = buys - 1

            if len(k2Array) > 0:
                if len(k2Array) >= buys:
                    divider = buys
                    for papers in k2Array:
                        if buys > 0:
                            retArray.append([arrayNames[papers], "K", str(75 / divider)])
                            buys = buys - 1
                elif len(k2Array) >= buys / 2:
                    divider = len(k2Array)
                    for papers in k2Array:
                        retArray.append([arrayNames[papers], "K", str(50 / divider)])
                        buys = buys - 1

                    if len(k1Array) > 0:
                        if len(k1Array) >= buys:
                            divider = buys
                            for papers in k1Array:
                                if buys > 0:
                                    retArray.append([arrayNames[papers], "K", str(25 / divider)])
                                    buys = buys - 1
                        else:
                            divider = len(k1Array)
                            for papers in k1Array:
                                retArray.append([arrayNames[papers], "K", str(10 / divider)])
                                buys = buys - 1
                            if len(k0Array) > 0:
                                if len(k0Array) > buys:
                                    divider = buys
                                else:
                                    divider = len(k0Array)
                                for papers in k0Array:
                                    if buys > 0:
                                        retArray.append([arrayNames[papers], "K", str(5 / divider)])
                                        buys = buys - 1
                    else:
                        if len(k0Array) > 0:
                            if len(k0Array) > buys:
                                divider = buys
                            else:
                                divider = len(k0Array)
                            for papers in k0Array:
                                if buys > 0:
                                    retArray.append([arrayNames[papers], "K", str(7.5 / divider)])
                                    buys = buys - 1

                                    # extend evt 7777
                else:
                    divider = len(k2Array)
                    for papers in k2Array:
                        retArray.append([arrayNames[papers], "K", str(15 / divider)])
                        buys = buys - 1

                    if len(k1Array) > 0:
                        if len(k1Array) >= buys:
                            divider = buys
                            for papers in k1Array:
                                if buys > 0:
                                    retArray.append([arrayNames[papers], "K", str(10 / divider)])
                                    buys = buys - 1

                        else:
                            divider = len(k1Array)
                            for papers in k1Array:
                                retArray.append([arrayNames[papers], "K", str(5 / divider)])
                                buys = buys - 1
                            if len(k0Array) > 0:
                                if len(k0Array) > buys:
                                    divider = buys
                                else:
                                    divider = len(k0Array)
                                for papers in k0Array:
                                    if buys > 0:
                                        retArray.append([arrayNames[papers], "K", str(2.5 / divider)])
                                        buys = buys - 1
            else:
                if len(k1Array) > 0:
                    if len(k1Array) >= buys:
                        divider = buys
                        for papers in k1Array:
                            if buys > 0:
                                retArray.append([arrayNames[papers], "K", str(12.5 / divider)])
                                buys = buys - 1
                    else:
                        divider = len(k1Array)
                        for papers in k1Array:
                            retArray.append([arrayNames[papers], "K", str(7.5 / divider)])
                            buys = buys - 1
                        if len(k0Array) > 0:
                            if len(k0Array) >= buys:
                                divider = buys
                                for papers in k0Array:
                                    if buys > 0:
                                        retArray.append([arrayNames[papers], "K", str(5 / divider)])
                                        buys = buys - 1
                            else:
                                divider = len(k0Array)
                                for papers in k0Array:
                                    if buys > 0:
                                        retArray.append([arrayNames[papers], "K", str(3.5 / divider)])
                                        buys = buys - 1
                else:
                    if len(k0Array) > 0:
                        if len(k0Array) > buys:
                            divider = buys
                        else:
                            divider = len(k0Array)
                        for papers in k0Array:
                            if buys > 0:
                                retArray.append([arrayNames[papers], "K", str(5 / divider)])
                                buys = buys - 1


    elif len(k2Array) > 0:

        if len(v2Array) > 0:
            for papers in v2Array:
                retArray.append([arrayNames[papers], "V", "100"])
        if len(v1Array) > 0:
            for papers in v1Array:
                retArray.append([arrayNames[papers], "V", "75"])
                # sell(arrayNames[papers],75)
        if len(v0Array) > 0:
            for papers in v0Array:
                retArray.append([arrayNames[papers], "V", "50"])
        if len(h0Array) > 0:
            for papers in h0Array:
                retArray.append([arrayNames[papers], "V", "25"])
        if len(k2Array) >= buys:
            divider = buys
            for papers in k2Array:
                if buys > 0:
                    retArray.append([arrayNames[papers], "K", str(100 / divider)])
                    buys = buys - 1
        elif len(k2Array) >= buys / 2:
            divider = len(k2Array)
            for papers in k2Array:
                retArray.append([arrayNames[papers], "K", str(75 / divider)])
                buys = buys - 1

            if len(k1Array) > 0:
                if len(k1Array) >= buys:
                    divider = buys
                    for papers in k1Array:
                        if buys > 0:
                            retArray.append([arrayNames[papers], "K", str(25 / divider)])
                            buys = buys - 1
                elif len(k1Array)> buys / 2:
                    divider = len(k1Array)
                    for papers in k1Array:
                        retArray.append([arrayNames[papers], "K", str(20 / divider)])
                        buys = buys - 1
                    if len(k0Array) > buys/2:
                        if len(k0Array) > buys:
                            divider = buys
                        else:
                            divider = len(k0Array)
                        for papers in k0Array:
                            if buys > 0:
                                retArray.append([arrayNames[papers], "K", str(5 / divider)])
                                buys = buys - 1
                    else:
                        divider = len(k0Array)
                        for papers in k0Array:
                            retArray.append([arrayNames[papers], "K", str(3 / divider)])
                            buys = buys - 1

                else:
                    divider = len(k1Array)
                    for papers in k1Array:
                        retArray.append([arrayNames[papers], "K", str(15 / divider)])
                        buys = buys - 1
                    if len(k0Array) > buys/2:
                        if len(k0Array) > buys:
                            divider = buys
                        else:
                            divider = len(k0Array)
                        for papers in k0Array:
                            if buys > 0:
                                retArray.append([arrayNames[papers], "K", str(5 / divider)])
                                buys = buys - 1
                    else:
                        divider = len(k0Array)
                        for papers in k0Array:
                            retArray.append([arrayNames[papers], "K", str(3 / divider)])
                            buys = buys - 1
            else:
                if len(k0Array) > buys / 2:
                    if len(k0Array) > buys:
                        divider = buys
                    else:
                        divider = len(k0Array)
                    for papers in k0Array:
                        if buys > 0:
                            retArray.append([arrayNames[papers], "K", str(10 / divider)])
                            buys = buys - 1
                else:
                    divider = len(k0Array)
                    for papers in k0Array:
                        retArray.append([arrayNames[papers], "K", str(5 / divider)])
                        buys = buys - 1

                        # extend evt 7777
        elif len(k2Array) >= buys / 4:
            divider = len(k2Array)
            for papers in k2Array:
                retArray.append([arrayNames[papers], "K", str(50 / divider)])
                buys = buys - 1

            if len(k1Array) > 0:
                if len(k1Array) >= buys:
                    divider = buys
                    for papers in k1Array:
                        if buys > 0:
                            retArray.append([arrayNames[papers], "K", str(50 / divider)])
                            buys = buys - 1
                elif len(k1Array) > buys / 2:
                    divider = len(k1Array)
                    for papers in k1Array:
                        retArray.append([arrayNames[papers], "K", str(35 / divider)])
                        buys = buys - 1
                    if len(k0Array) > buys / 2:
                        if len(k0Array) > buys:
                            divider = buys
                        else:
                            divider = len(k0Array)
                        for papers in k0Array:
                            if buys > 0:
                                retArray.append([arrayNames[papers], "K", str(7.5 / divider)])
                                buys = buys - 1
                    else:
                        divider = len(k0Array)
                        for papers in k0Array:
                            retArray.append([arrayNames[papers], "K", str(4 / divider)])
                            buys = buys - 1
                else:
                    divider = len(k1Array)
                    for papers in k1Array:
                        retArray.append([arrayNames[papers], "K", str(10 / divider)])
                        buys = buys - 1
                    if len(k0Array) > buys / 2:
                        if len(k0Array) > buys:
                            divider = buys
                        else:
                            divider = len(k0Array)
                        for papers in k0Array:
                            if buys > 0:
                                retArray.append([arrayNames[papers], "K", str(10 / divider)])
                                buys = buys - 1
                    else:
                        divider = len(k0Array)
                        for papers in k0Array:
                            retArray.append([arrayNames[papers], "K", str(5 / divider)])
                            buys = buys - 1
        else:
            divider = len(k2Array)
            for papers in k2Array:
                retArray.append([arrayNames[papers], "K", str(25 / divider)])
                buys = buys - 1

            if len(k1Array) > 0:
                if len(k1Array) >= buys:
                    divider = buys
                    for papers in k1Array:
                        if buys > 0:
                            retArray.append([arrayNames[papers], "K", str(55 / divider)])
                            buys = buys - 1

                elif len(k1Array) > buys / 2:
                    divider = len(k1Array)
                    for papers in k1Array:
                        retArray.append([arrayNames[papers], "K", str(40 / divider)])
                        buys = buys - 1
                    if len(k0Array) > buys / 2:
                        if len(k0Array) > buys:
                            divider = buys
                        else:
                            divider = len(k0Array)
                        for papers in k0Array:
                            if buys > 0:
                                retArray.append([arrayNames[papers], "K", str(7.5 / divider)])
                                retArray.append(arrayNames[papers], "K", 7.5 / divider)
                                buys = buys - 1
                    else:
                        divider = len(k0Array)
                        for papers in k0Array:
                            retArray.append([arrayNames[papers], "K", str(4 / divider)])
                            buys = buys - 1

                else:
                    divider = len(k1Array)
                    for papers in k1Array:
                        retArray.append([arrayNames[papers], "K", str(15 / divider)])
                        buys = buys - 1
                    if len(k0Array) > buys / 2:
                        if len(k0Array) > buys:
                            divider = buys
                        else:
                            divider = len(k0Array)
                        for papers in k0Array:
                            if buys > 0:
                                retArray.append([arrayNames[papers], "K", str(7.5 / divider)])
                                buys = buys - 1
                    else:
                        divider = len(k0Array)
                        for papers in k0Array:
                            retArray.append([arrayNames[papers], "K", str(4 / divider)])
                            buys = buys - 1

    elif len(k1Array) > 0:
        if len(v2Array)>0:
            for papers in v2Array:
                retArray.append([arrayNames[papers], "V", "75"])
        if len(v1Array) > 0:
            for papers in v1Array:
                retArray.append([arrayNames[papers], "V", "50"])
        if len(v0Array) > 0:
            for papers in v0Array:
                retArray.append([arrayNames[papers], "V", "25"])
        if len(k1Array) >= buys:
            divider = buys
            for papers in k1Array:
                if buys > 0:
                    retArray.append([arrayNames[papers], "K",  str(75 / divider)])
                    buys = buys - 1
        elif len(k1Array) > buys / 2:
            divider = len(k1Array)
            for papers in k1Array:
                retArray.append([arrayNames[papers], "K", str(50 / divider)])
                buys = buys - 1
            if len(k0Array) >= buys:
                divider = buys
                for papers in k0Array:
                    if buys > 0:
                        retArray.append([arrayNames[papers], "K", str(15 / divider)])
                        buys = buys - 1
            elif len(k0Array) > buys / 2:
                if len(k0Array) > buys:
                    divider = buys
                else:
                    divider = len(k0Array)
                for papers in k0Array:
                    if buys > 0:
                        retArray.append([arrayNames[papers], "K", str(10 / divider)])
                        buys = buys - 1
            elif len(k0Array) > buys / 4:
                if len(k0Array) > buys:
                    divider = buys
                else:
                    divider = len(k0Array)
                for papers in k0Array:
                    if buys > 0:
                        retArray.append([arrayNames[papers], "K", str(5 / divider)])
                        buys = buys - 1
            else:
                divider = len(k0Array)
                for papers in k0Array:
                    retArray.append([arrayNames[papers], "K", str(2.5 / divider)])
                    buys = buys - 1

        elif len(k1Array) > buys / 4:
            divider = len(k1Array)
            for papers in k1Array:
                retArray.append([arrayNames[papers], "K", str(25 / divider)])
                buys = buys - 1
            if len(k0Array) >= buys:
                divider = buys
                for papers in k0Array:
                    if buys > 0:
                        retArray.append([arrayNames[papers], "K", str(17 / divider)])
                        buys = buys - 1
            elif len(k0Array) > buys / 2:
                if len(k0Array) > buys:
                    divider = buys
                else:
                    divider = len(k0Array)
                for papers in k0Array:
                    if buys > 0:
                        retArray.append([arrayNames[papers], "K", str(12 / divider)])
                        buys = buys - 1
            elif len(k0Array) > buys / 4:
                if len(k0Array) > buys:
                    divider = buys
                else:
                    divider = len(k0Array)
                for papers in k0Array:
                    if buys > 0:
                        retArray.append([arrayNames[papers], "K", str(5 / divider)])
                        buys = buys - 1
            else:
                divider = len(k0Array)
                for papers in k0Array:
                    retArray.append([arrayNames[papers], "K", str(2.5 / divider)])
                    buys = buys - 1
        else:
            divider = len(k1Array)
            for papers in k1Array:
                retArray.append([arrayNames[papers], "K", str(25 / divider)])
                buys = buys - 1
            if len(k0Array) > buys / 2:
                if len(k0Array) > buys:
                    divider = buys
                else:
                    divider = len(k0Array)
                for papers in k0Array:
                    if buys > 0:
                        retArray.append([arrayNames[papers], "K", str(17 / divider)])
                        buys = buys - 1
            elif len(k0Array) > buys / 4:
                if len(k0Array) > buys:
                    divider = buys
                else:
                    divider = len(k0Array)
                for papers in k0Array:
                    if buys > 0:
                        retArray.append([arrayNames[papers], "K", str(5 / divider)])
                        buys = buys - 1
            else:
                if len(k0Array) > buys:
                    divider = buys
                else:
                    divider = len(k0Array)
                for papers in k0Array:
                    retArray.append([arrayNames[papers], "K", str(2.5 / divider)])
                    buys = buys - 1
    elif len(k0Array) > 0:
        if len(v2Array) > 0:
            for papers in v2Array:
                retArray.append([arrayNames[papers], "V", "50"])
        if len(v1Array) > 0:
            for papers in v1Array:
                retArray.append([arrayNames[papers], "V", "25"])
        if len(k0Array) >= buys:
            divider = buys
            for papers in k0Array:
                if buys > 0:
                    retArray.append([arrayNames[papers], "K", str(40 / divider)])
                    buys = buys - 1
        elif len(k0Array) > buys / 2:
            if len(k0Array) > buys:
                divider = buys
            else:
                divider = len(k0Array)
            for papers in k0Array:
                if buys > 0:
                    retArray.append([arrayNames[papers], "K", str(30 / divider)])
                    buys = buys - 1
        elif len(k0Array) > buys / 4:
            if len(k0Array) > buys:
                divider = buys
            else:
                divider = len(k0Array)
            for papers in k0Array:
                if buys > 0:
                    retArray.append([arrayNames[papers], "K", str(20 / divider)])
                    buys = buys - 1
        else:
            divider = len(k0Array)
            for papers in k0Array:
                retArray.append([arrayNames[papers], "K", str(10 / divider)])
                buys = buys - 1

    return retArray

Names = ["ze", "one", "two", "three", "fo", "fi", "si", "se", "eig", "ni", "te", "el", "tw", "thi", "fourt", "fivt", "sixt", "Sevt"]
states1 = ["V0", "V1", "V2", "V3", "H0", "H1", "H2", "H3", "V0", "V1", "V2", "V3", "H0", "H1", "H2", "H3", "V0", "K3"]
states = ["V3", "K3", "K2", "K3", "K0", "K1", "K2", "K2", "K0", "K1", "K2", "K3", "K0", "K1", "K2", "K2", "K2", "K3"]
print(len(states))
print(len(Names))
print(getTransactions(Names, states, 15))