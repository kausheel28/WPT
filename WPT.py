import pandas as pd
import re
import requests
file1 = open('myfile.txt', 'r') 
lines = file1.readlines() 
print(lines)
with pd.ExcelWriter('./datasets/Test.xlsx',mode='w',engine='openpyxl') as writer:
    for url in lines:
        url=re.sub("\n",'',url)  
        print(url)
        l=str(url)
        u=l[30:len(l)-1]
        print(u)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
        page = requests.get(url,headers=headers)
        fv= pd.read_html(page.content)[0]
        df=pd.DataFrame(fv)
        df.columns=['Step','First Byte','Start Render','FCP','SI','LCP','CLS','TBT','TTI','R','B','T','Re','By']
        dff=df
        dfn=dff[['Step','SI','LCP','CLS','TBT','TTI']]
        i = dfn[(dfn.Step == 'First View')].index
        dfn=dfn.drop(i)
        j= dfn[(dfn.Step == 'Repeat View')].index
        dfn=dfn.drop(j)
        t=True
        filtersymbol=dfn['TBT'].str.contains('≥')
        dfn=dfn.replace('-','0.00s')
        
        if filtersymbol.any()==t:
            dfn['TBT'] = dfn['TBT'].map(lambda x: x[1:])
            dfn=dfn.replace(' -','0.00s')


        dfn['LCP'] = dfn['LCP'].map(lambda x: x.rstrip('s')).astype('float64')
        dfn['SI'] = dfn['SI'].map(lambda x: x.rstrip('s')).astype('float64')
        dfn['TTI'] = dfn['TTI'].map(lambda x: x.rstrip('s')).astype('float64')
        dfn['TBT'] = dfn['TBT'].map(lambda x: x.rstrip('s')).astype('float64')
        dfn['CLS']=dfn['CLS'].astype('float64')

        dfn['WCV']=dfn['SI']*0.25 + dfn['LCP']*0.25 + dfn['CLS']*0.05 + dfn['TBT']*0.25 + dfn['TTI']*0.20


        print('Data Exported to EXCEL file started')
        sheet_name='WCV'+str(u)
        print(sheet_name)

        dfn.to_excel(writer, sheet_name='WCV'+str(u),index=False)
        writer.save()
        print('Data Exported to EXCEL file ended')
        x=True
        pattern3="LandingPage1|LandingPage2|LandingPage3|LandingPage4|LandingPage5|LandingPage6|LandingPage7|LandingPage8"




        filter3=dfn['Step'].str.contains(pattern3)


        if filter3.any()==x:
            df4=dfn[filter3]
            new_row3 = {'Step':'LandingPage(avg)', 'SI':df4['SI'].mean(), 'LCP':df4['LCP'].mean(), 'CLS':df4['CLS'].mean(), 'TBT':df4['TBT'].mean(), 'TTI':df4['TTI'].mean(), 'WCV':df4['WCV'].mean()}
            df4 = df4.append(new_row3, ignore_index=True)
            df4.to_excel(writer, sheet_name='LandingPage(avg)',index=False)
        else:
            print("NO PDP")

# Close the Pandas Excel writer and output the Excel file.

        writer.save()
        print('Data eported tab2')


