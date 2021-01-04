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
        pattern="PLP-Major1|PLP-Major2|PLP-Major3|PLP-Major4|PLP-Major5|PLP-Major6"
        pattern2="PLP-Minor1|PLP-Minor2|PLP-Minor3|PLP-Minor4|PLP-Minor5|PLP-Minor6"
        pattern3="LandingPage1|LandingPage2|LandingPage3|LandingPage4|LandingPage5|LandingPage6|LandingPage7|LandingPage8"
        pattern4="PDP-Major1|PDP-Major2|PDP-Major3|PDP-Major4|PDP-Major5|PDP-Major6"
        pattern5="PDP-Minor1|PDP-Minor2|PDP-Minor3|PDP-Minor4|PDP-Minor5|PDP-Minor6"


        filter1=dfn['Step'].str.contains(pattern)
        filter2=dfn['Step'].str.contains(pattern2)
        filter3=dfn['Step'].str.contains(pattern3)
        filter4=dfn['Step'].str.contains(pattern4)
        filter5=dfn['Step'].str.contains(pattern5)

        if filter1.any()==x:
            df2=dfn[filter1]
            new_row1 = {'Step':'PLP-Major(avg)', 'SI':df2['SI'].mean(), 'LCP':df2['LCP'].mean(), 'CLS':df2['CLS'].mean(), 'TBT':df2['TBT'].mean(), 'TTI':df2['TTI'].mean(), 'WCV':df2['WCV'].mean()}
            df2 = df2.append(new_row1, ignore_index=True)
            df2.to_excel(writer, sheet_name='PLP-Major(avg)',index=False)

        if filter2.any()==x:
            df3=dfn[filter2]
            new_row2 = {'Step':'PLP-Minor(avg)', 'SI':df3['SI'].mean(), 'LCP':df3['LCP'].mean(), 'CLS':df3['CLS'].mean(), 'TBT':df3['TBT'].mean(), 'TTI':df3['TTI'].mean(), 'WCV':df3['WCV'].mean()}
            df3 = df3.append(new_row2, ignore_index=True)
            df3.to_excel(writer, sheet_name='PLP-Minor(avg)',index=False)

        if filter3.any()==x:
            df4=dfn[filter3]
            new_row3 = {'Step':'LandingPage(avg)', 'SI':df4['SI'].mean(), 'LCP':df4['LCP'].mean(), 'CLS':df4['CLS'].mean(), 'TBT':df4['TBT'].mean(), 'TTI':df4['TTI'].mean(), 'WCV':df4['WCV'].mean()}
            df4 = df4.append(new_row3, ignore_index=True)
            df4.to_excel(writer, sheet_name='LandingPage(avg)',index=False)


        if filter4.any()==x:
            df5=dfn[filter4]
            new_row4 = {'Step':'PDP-Major(avg)', 'SI':df5['SI'].mean(), 'LCP':df5['LCP'].mean(), 'CLS':df5['CLS'].mean(), 'TBT':df5['TBT'].mean(), 'TTI':df5['TTI'].mean(), 'WCV':df5['WCV'].mean()}
            df5 = df5.append(new_row4, ignore_index=True)
            df5.to_excel(writer, sheet_name='PDP-Major(avg)',index=False)

        if filter5.any()==x:
            df6=dfn[filter5]
            new_row5 = {'Step':'PDP-Minor(avg)', 'SI':df6['SI'].mean(), 'LCP':df6['LCP'].mean(), 'CLS':df6['CLS'].mean(), 'TBT':df6['TBT'].mean(), 'TTI':df6['TTI'].mean(), 'WCV':df6['WCV'].mean()}
            df6 = df6.append(new_row5, ignore_index=True)
            df6.to_excel(writer, sheet_name='PDP-Minor(avg)',index=False)
        else:
            print("NO PDP")

# Close the Pandas Excel writer and output the Excel file.

        writer.save()
        print('Data eported tab2')


