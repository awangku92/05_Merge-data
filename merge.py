import pandas as pd
import os, glob

def merge_files():
    # GET PATH
    # os.getcwd() #get current working directory
    dataPath = os.path.join(os.getcwd(), "seperatedData")
    mergedPath = os.path.join(os.getcwd(), "merged.txt")

    #change dir to extracted file
    os.chdir(dataPath)

    # used to get all file extension .txt
    #fileList = glob.glob("*.txt")

    #init dataframe and get all file extension .txt into dataframe
    dfList = [f for f_ in [glob.glob(e) for e in ['*.txt']] for f in f_]
    # print(dfList)

    tempDf = []

    # loop filelist to merge all files
    for filename in dfList:
        # print(filename)
        df = pd.read_csv(filename, header=0)
        # print(df)
        tempDf.append(df)

    # merge file and save to .txt file
    mergeDf = pd.concat(tempDf,axis=0) # axis=0 ==> merge vertical 
    # print(mergeDf)
    mergeDf.to_csv(mergedPath, index=None)

    return

def merge_file_horizontal():
    filelist=glob.glob("C:\\Exercise\\*.xls")
    dfList=[]
    for filename in filelist:
        df=pd.read_excel(filename,skiprows=[0,1,2])
        dfList.append(df)
        concatDf=pd.concat(dfList,axis=1) # axis=1 ==> merge horizontal
        concatDf.to_csv("C:\\Exercise\\IncomeByStateByYear.csv",index=0)

    return

def merge_file_on_matching_col():
    leftDf=pd.read_csv("<file_path>")

    # converters convert data to required datatype
    rightDf=pd.read_csv("<file_path>", converters={"col1":str, "col2":str})  

    # create new column
     rightDf["new_col"] = rightDf["col1"]+"-"+rightDf["col2"]

     # df.ix is deprecated, use iloc[] @ loc[] instead - is used for splicing df 
     #  left_on & right_on is used to merge on that col 
     mergeDf=pd.merge(leftDf,rightDf.ix[:,["new_col","col3","col4"]], left_on="col", right_on="new_col")
     # set specified col as index/begining of col 
     mergeDf.set_index(["col","new_col"], inplace=True)
     mergeDf.to_csv("<output_file>")

    return

def remove_duplicate_col():
    concatDf=pd.read_csv("C:\\Exercise\\IncomeByStateByYear.csv")
    #remove dups
    # drop_duplicates removes rows, to remove col, use T method to transpose df, remove cols, then transpose again
    nodupl=concatDf.T.drop_duplicates().T
    nodupl.to_csv("C:\\Exercise\\IncomeByStateByYearNoDupl.csv",index=0)

    return


# main method
def main():
    merge_files()
    # merge_files_horizontal()
    # merge_file_on_matching_col()
    # remove_duplicate_col()

if __name__ == '__main__':
    main()