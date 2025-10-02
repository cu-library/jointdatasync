import NZ_Script_1
import OCLC_doublecheck
import NZ_Script_2
import os

def main():
    try:
        #Check for inputs folder and quit if not present
        if not os.path.exists('./Inputs'):
            print('Error: Please create a folder named "Inputs" populated with OCLC bib processing reports in the current directory')
            exit()

        #Check for outputs folder and create if missing
        if not os.path.exists('./Outputs'):
            print("Creating output folder...")
            os.makedirs("./Outputs")

        #Run script one (merging reports and comparing incoming OCLC numbers to find updated records)
        print("Running NZ_Script_1...")
        NZ_Script_1.merge_reports()
        print("Reports merged. Comparing OCLC #s...")
        NZ_Script_1.compare_OCLC()

        #Collect data from Analytics to check current OCLC #s against OCLC reports
        print("Obtaining OCLC doublecheck data...")
        OCLC_doublecheck_df = OCLC_doublecheck.get_OCLC_doublecheck()
        OCLC_doublecheck.write_doublecheck_to_excel(OCLC_doublecheck_df)

        #Produce reports for processing in Alma
        print("Running NZ_Script_2...")
        NZ_Script_2.create_reports()

    except Exception as e:
        print(e)
        pass

if __name__ == "__main__":
    main()
