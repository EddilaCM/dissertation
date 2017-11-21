# __author__ = 'Administrator'
# -*- coding:utf-8 -*-
import returnHTML
from lxml import etree
import xlwt
import re


class lagou:

    def __init__(self):
        self.Url_1 = "https://www.lagou.com/"
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                       # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                       # 'Accept-Charset': 'zh-CN,zh;q=0.8,en;q=0.6',
                       # 'Accept_Encoding': 'gzip, deflate, br',
                       # 'Connection':'keep-alive',
                       # 'Host':'www.lagou.com'
                       }

    def getfirst(self):
        nameArrE = ['class_one','class_two','class_three','Job_name', 'job_company', 'job_link', 'low_salary', 'job_release_time', 'job_experience',
                'job_edu', 'job_area', 'job_welfare']
        JobBook = xlwt.Workbook(encoding='utf-8', style_compression=0)
        # 打开工作簿
        # JobBook = xlrd.open_workbook('laGou_JobList_all_1.xls','w')
        # 添加一个sheet
        job_sheet = JobBook.add_sheet('job_time', cell_overwrite_ok=True)
        for x in range(0,len(nameArrE),1):
            job_sheet.write(0,x,nameArrE[x])
        i = 1
        # User_Agent, Accept, Accept_Charset, Accept_Encoding, Host,url,IPPool,enable_proxy
        IpPool = self.getIpPool()
        html1=returnHTML.ReturnHTML(self.header,self.Url_1,IpPool,True)
        html = html1.IPPool_browser()
        first_tree = etree.HTML(html)
        class1 = first_tree.xpath('//div[@class="menu_main job_hopping"]/div[@class="category-list"]/h2/text()')
        typeOne =[]
        if len(class1)!=0:
            for class1_1 in class1:
                aa = self.removeSpace(class1_1)
                if aa != "":
                    typeOne.append(aa)
            # print(len(typeOne))
            for x in range(0, len(class1), 1):
                type_big_tree = first_tree.xpath('//div[@class="menu_box"]')[x]
                # 一级分类
                class_one_x_text = typeOne[x]
                class_twoAndthree_x = type_big_tree.xpath('div[@class="menu_sub dn"]/dl')
                # print(len(class_twoAndthree_x))
                for b in class_twoAndthree_x:
                    class_two = b.xpath('dt/span/text()')[0]
                    # print('classTwo:', class_two)
                    class_three_list = b.xpath('dd/a')
                    for c in class_three_list:
                        class_three = c.text
                        print class_three
                        three_url = c.xpath('@href')[0]
                        print("3_url:" + three_url)
                        para1={'px': 'default', 'city': '全国'}
                        sencondHtmlObject = returnHTML.ReturnHTML(self.header,three_url,IpPool,True)
                        sencondHtml = sencondHtmlObject.rqsWay_IpPool_Brower('get',para1)
                        secondTree = etree.HTML(sencondHtml)
                        # job列表
                        # print sencondHtml
                        # nuber_a = len(secondTree.xpath('//div[@class="item_con_pager"]/div[@class="pager_container"]/a'))-1
                        # print nuber_a
                        # total_page1 = secondTree.xpath('//div[@class="item_con_pager"]/div[@class="pager_container"]/a['+str(nuber_a)+']/@data-index')
                        # print total_page1
                        # total_page = int(total_page1[0])
                        total_page = 30
                        pre_url = three_url
                        if int(total_page) >= 1:
                            for page in xrange(1, (int(total_page)+1), 1):
                                this_url = pre_url + str(page) + '/'
                                para={'px': 'default', 'city': '全国'}
                                # if page ==1:
                                #     para['filterOption'] = 1
                                # elif page==2:
                                #     para['filterOption'] = 2
                                # else:
                                #     para['filterOption'] = 3
                                # para={'px': 'default', 'city': '全国', 'labelWords': 'label'}
                                listPageObject = returnHTML.ReturnHTML(self.header,this_url,IpPool,True)
                                listPageHtml = listPageObject.rqsWay_IpPool_Brower("get", para)
                                # listPageHtml = listPageObject.IPPool_browser()
                                listPageTree = etree.HTML(listPageHtml)
                                li_list = listPageTree.xpath('//div[@id="s_position_list"]/ul[@class="item_con_list"]/li[@class="con_list_item default_list"]')
                                # print(len(li_list))
                                for x in range(0,len(li_list),1):
                                    current_li = li_list[x]
                                    # 工作名称
                                    job_name =current_li.xpath('@data-positionname')[0]
                                    # 公司
                                    job_company =current_li.xpath('@data-company')[0]
                                    # 链接
                                    job_link ='https://www.lagou.com/jobs/'+str(current_li.xpath('@data-positionid')[0])+'.html'
                                    # 工资
                                    job_salary =current_li.xpath('@data-salary')[0]
                                    low_salary =(job_salary.split('-'))[0].replace("K",'').replace("k","")
                                    # 发布时间
                                    job_release_time =current_li.xpath('div[@class="list_item_top"]/div[@class="position"]/div[@class="p_top"]/span[@class="format-time"]/text()')[0]
                                    #工作经验、学历
                                    job_experience_edu =current_li.xpath('div[@class="list_item_top"]/div[@class="position"]/div[@class="p_bot"]/div[@class="li_b_l"]/text()')
                                    job_experience_edu1 = job_experience_edu[len(job_experience_edu)-1].strip()
                                    job_experience = (job_experience_edu1.split("/"))[0]
                                    job_edu = (job_experience_edu1.split("/"))[1]
                                    # 工作地
                                    job_area = current_li.xpath('div[@class="list_item_top"]/div[@class="position"]/div[@class="p_top"]/a[@class="position_link"]/span[@class="add"]/em/text()')[0]
                                    # 福利
                                    job_welfare = current_li.xpath('div[@class="list_item_bot"]/div[@class="li_b_r"]/text()')[0]
                                    # 添加数据
                                    job_sheet.write(i, 0, class_one_x_text)
                                    job_sheet.write(i, 1, class_two)
                                    job_sheet.write(i, 2, class_three)
                                    job_sheet.write(i, 3, job_name)
                                    job_sheet.write(i, 4, job_company)
                                    job_sheet.write(i, 5, job_link)
                                    job_sheet.write(i, 6, low_salary)
                                    job_sheet.write(i, 7, job_release_time)
                                    job_sheet.write(i, 8, job_experience)
                                    job_sheet.write(i, 9, job_edu)
                                    job_sheet.write(i, 10, job_area)
                                    job_sheet.write(i, 11, job_welfare)
                                    i += 1
                                    JobBook.save('dataFile/laGou_JobList_all20171108_3.xls')
        else:
            print(u"没有一级分类的数据！！！")

    def getIpPool(self):
        urlPool = []
        IPS = file('ip.txt','r')
        for ip in IPS:
            ip = ip.replace('\n','')
            urlPool.append(ip)
        IPS.close()
        urlPool = self.del_ips(urlPool)
        return urlPool

    def del_ips(self,ips):
        delips = ['110.72.182.21:8123','112.85.9.216:808', '61.188.24.232:808',
              '114.239.146.47:808','180.123.175.58:8998','222.94.151.198:808',
               '122.245.66.87:808','171.39.72.33:8123','180.121.163.229:808',
              '115.220.2.167:808','175.155.25.53:808','175.155.243.68:808']
        for ip in ips:
            for delete in delips:
                if ip == delete:
                    ips.remove(ip)
        return ips

    def removeSpace(self,para):
        a = para.replace('\n','')
        return a.strip()

    def CreatExcel(self,sheetName,titles):
        # 创建工作簿
        JobBook = xlwt.Workbook(encoding='utf-8', style_compression=0)
        # 打开工作簿
        # JobBook = xlrd.open_workbook('laGou_JobList_all_1.xls','w')
        # 添加一个sheet
        job_sheet = JobBook.add_sheet(sheetName, cell_overwrite_ok=True)
        for x in range(0,len(titles),1):
            job_sheet.write(0,x,titles[x])
        return sheetName,JobBook

    # 去掉斜杠
    def del_dip(self,arg):
        arg = arg.replace('/', '')
        return arg

    # 去掉“经验”或“招聘”
    def del_experience(self,arg):
        arg = re.sub(u'经验', '', arg)
        return arg

    def del_recruit(self,arg):
        arg = re.sub(u'招聘', '', arg)
        return arg
test1 = lagou()
test1.getfirst()
