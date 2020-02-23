# This program checks raw output from Cisco NXOS and searches for a particular string. It then outputs a csv file
# that collates the results of each test.
# Jim Mangafas
# Version 0.1
# Used on switch Cisco 9200 & 9300 switches.

#Libraries
import csv
import glob

#get list of existing switch output
for files in glob.glob('*.txt'):
    i = open(files, 'r')
    i_content = i.readlines()

#variables
    vtp = "VTP version running             : 3"
    vlan = "Trunking Native Mode VLAN: 999 (Native)"
    mode = "VTP Operating Mode                : Client"
    mst = "Switch is in mst mode (IEEE Standard)"
    root1 = "Address     10b3.d5a4.e220"
    root2 = "Address     084f.a93d.7380"
    uplink1 = "Te1/1/1     Active"
    uplink2 = "Te2/1/1     Active"
    uplink2s1 = "Te1/1/2     Active"
    hostname = (i_content[6][:24])

#Open each text file and evaluate if criteria is met.
    with open('Layer2_Testing.csv', 'a', newline='') as Layer2_Testing:
        thewriter = csv.writer(Layer2_Testing)

        if any(vtp in line for line in i_content):
            print(f"{vtp} : Has been found")
            vtp_result = '3'

        else:
            print(f"{vtp} : Not found")
            vtp_result = 'Not Found'

        if any(vlan in line for line in i_content):
            print(f"{vlan} : Has been found")
            vlan_result = '999'

        else:
            print(f"{vlan} : Not found")
            vlan_result = 'Not Found'

        if any(mode in line for line in i_content):
            print(f"{mode} : Has been found")
            mode_result = 'Client'

        else:
            print(f"{mode} : Not found")
            mode_result = 'Not Found'

        if any(mst in line for line in i_content):
            print(f"{mst} : Has been found")
            mst_result = 'Enabled'

        else:
            print(f"{mst} : Not found")
            mst_result = 'Not Active'

        if any(root1 in line for line in i_content):
            print(f"Root {root1} : Has been found")
            root1_result = 'Dist S1'

        else:
            print(f"{root1} : Not found")
            root1_result = 'Not Found'

        if any(root2 in line for line in i_content):
            print(f"Root {root2} : Has been found")
            root2_result = 'Dist S2'

        else:
            print(f"{root2} : Not found")
            root2_result = 'Not Found'

        if any(uplink1 in line for line in i_content):
            print(f"Uplink {uplink1} : Has been found")
            uplink1_result = 'Active'

        else:
            print(f"Uplink {uplink1} : Not found")
            uplink1_result = 'Not Active'

        if any(uplink2 in line for line in i_content):
            print(f"Uplink {uplink2} : Has been found")
            uplink2_result = 'Active'

        else:
            print(f"Uplink {uplink2} : Not found")
            uplink2_result = 'Not Active'

        if any(uplink2s1 in line for line in i_content):
            print(f"Uplink {uplink2s1} : Has been found")
            uplink2s1_result = 'Active'

        else:
            print(f"Uplink {uplink2s1} : Not found")
            uplink2s1_result = 'Not Active'

#Write the results to the CSV file.
        thewriter.writerow([hostname, vtp_result, vlan_result, mode_result, mst_result, root1_result, root2_result, uplink1_result, uplink2_result, uplink2s1_result])

#Advise of completion so hostname can be linked the filename.
    print("\n"f"Checks completed for {hostname}""\n")
    print(files)

#Close both data files
    i.close()
Layer2_Testing.close()


