# __author__ = 'cm'
# -*- coding:utf-8 -*-
import returnEtree
import xlwt
import re
import error302


def del_ips(ips):
    delips = ['110.72.182.21:8123','112.85.9.216:808', '61.188.24.232:808',
              '114.239.146.47:808','180.123.175.58:8998','222.94.151.198:808',
               '122.245.66.87:808','171.39.72.33:8123','180.121.163.229:808',
              '115.220.2.167:808','175.155.25.53:808','175.155.243.68:808']
    for ip in ips:
        for delete in delips:
            if ip == delete:
                ips.remove(ip)
    return ips


def removeSpace(para):
    a = para.replace('\n','')
    return a.strip()


def del_ips(ips):
    delips = ['110.72.182.21:8123','112.85.9.216:808', '61.188.24.232:808',
              '114.239.146.47:808','180.123.175.58:8998','222.94.151.198:808',
               '122.245.66.87:808','171.39.72.33:8123','180.121.163.229:808',
              '115.220.2.167:808','175.155.25.53:808','175.155.243.68:808']
    for ip in ips:
        for delete in delips:
            if ip == delete:
                ips.remove(ip)
    return ips


# 去掉斜杠
def del_dip(arg):
    arg = arg.replace('/', '')
    return arg


# 去掉“经验”或“招聘”
def del_experience(arg):
    arg = re.sub(u'经验', '', arg)
    return arg


def del_recruit(arg):
    arg = re.sub(u'招聘', '', arg)
    return arg


def main():
    # header message
    Url = "https://www.lagou.com/"
    User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    Accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    Accept_Charset = 'zh-CN,zh;q=0.8,en;q=0.6',
    Accept_Encoding = 'gzip, deflate, sdch, br'
    Host = 'www.lagou.com'
    IPS = file('ip.txt','r')
    # 创建工作簿
    JobBook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    # 打开工作簿
    # JobBook = xlrd.open_workbook('laGou_JobList_all_1.xls','w')
    # 添加一个sheet
    job_sheet = JobBook.add_sheet('jobs_5', cell_overwrite_ok=True)
    # job_sheet = JobBook.sheet_by_index(1)
    # 定义表头
    is_English = False
    nameArrC = ['类2','类3','职位名称', '薪资', '工作地', '经验', '学历', '职位类别', '公司名称','链接','发布时间']
    nameArrE = ['class_two','class_three','Job_name', 'Job_salary', 'Job_area', 'Job_experience', 'Job_education', 'Job_type',
                'Company_name', 'detail_adder','link_addr']
    nameArr = []
    if is_English:
        nameArr = nameArrE
    else:
        nameArr = nameArrC
    attr = 0
    for x in range(0, len(nameArr), 1):
        job_sheet.write(0, x, nameArr[x])
    i = 1
    # 第一级分类
    typeOne=[]
    urlPool = []
    for ip in IPS:
        ip = ip.replace('\n','')
        urlPool.append(ip)
    IPS.close()
    urlPool = del_ips(urlPool)
    my_big_tree = returnEtree.header_browser(True, urlPool, Url, User_Agent, Accept, Accept_Charset, Accept_Encoding, Host)
    class1 = my_big_tree.xpath('//div[@class="menu_main job_hopping"]/div[@class="category-list"]/h2/text()')
    for x in range(0,len(class1),1):
        class_one=class1[x].strip()
        class2_1 = my_big_tree.xpath('//div[@class="menu_sub dn"]')[x]
        class2 = class2_1.xpath('dl/dt/span/text()')
        # print(class2)
        for y in range(0,len(class2),1):
            class_two=class2[y].strip()
            class3=class2_1.xpath('dl/dd/a/text()')
            class3Url=class2_1.xpath('dl/dd/a/@href')
            for three,url1 in zip(class3,class3Url):
                class_three = three.strip()
                newurl = url1
                # newurl = error302.getUnRedirectUrl(url1)
                print(newurl)
                list_page_node = returnEtree.header_browser(True, urlPool, newurl, User_Agent, Accept, Accept_Charset, Accept_Encoding, Host)
                total_page1 = list_page_node.xpath('//div[@class="pager_container"]/a[(last()-1)]/text()')[0]
                print(total_page1)
                if total_page1>=1:
                    for z in range(2,int(total_page1),1):
                        page_url = url1+str(z)+"/"
                        print(page_url)
                        para = {'filterOption':3}
                        this_page_job_list = returnEtree.header_browser_nourl_pool(page_url, User_Agent, Accept, Accept_Charset, Accept_Encoding, Host)
                        print(this_page_job_list)
                        job_num_this= this_page_job_list.xpath('//div[@id="s_position_list"]/ul[@class="item_con_list"]/li[@class="con_list_item default_list"]')
                        list_num = len(job_num_this)
                        print(list_num)
                        if list_num>=1:
                            for m in range(0,int(list_num),1):
                                Job_name_list = this_page_job_list.xpath('//li[@class="con_list_item default_list"]/@data-positionname')[m]
                                print(Job_name_list)
                                Job_salary_list = this_page_job_list.xpath('//li[@class="con_list_item default_list"]/@data-salary')[m]
                                print(Job_salary_list)
                                Job_Company_list = this_page_job_list.xpath('//li[@class="con_list_item default_list"]/@data-company')[m]
                                print(Job_Company_list)
                                this_li = this_page_job_list.xpath('//li[@class="con_list_item default_list"]')
                                for li_now in range(0,len(this_li),1):
                                    Job_area = li_now.xpath('a[@class="position_link"]/span[@class="add"]/em/text()')
                                    print(Job_area)
                                    release_time= li_now.xpath('span[@class="format-time"]/text()')
                                    Job_experience_and_edu = li_now.xpath('div[@class="p_bot"]/div[@class="li_b_l"]/text()')
                                    print(Job_experience_and_edu)
                                    Job_experience_and_edu1=Job_experience_and_edu.split("/")
                                    Job_experience = Job_experience_and_edu1[0]
                                    Job_edu = Job_experience_and_edu1[1]
                                # '类2','类3','职位名称', '薪资', '工作地', '经验', '学历', '职位类别', '公司名称','链接'
                                # job_sheet.write(i, 0, class_one_x_text)
                                job_sheet.write(i, 1, class_two)
                                job_sheet.write(i, 2, class_three)
                                job_sheet.write(i, 3, Job_name_list)
                                job_sheet.write(i, 4, Job_salary_list)
                                job_sheet.write(i, 5, Job_area)
                                job_sheet.write(i, 6, Job_experience)
                                job_sheet.write(i, 7, Job_edu)
                                # job_sheet.write(i, 8, del_dip(Job_type[0]))
                                job_sheet.write(i, 8, Job_Company_list)
                                job_sheet.write(i, 9, release_time)
                                # job_sheet.write(i, 11, Job_task)
                                # job_sheet.write(i, 12, detail_adder)
                                # job_sheet.write(i, 13, link)
                                i += 1
                                JobBook.save('dataFile/laGou_JobList_all20171029_2.xls')


                     # Job_area = list_page_node.xpath('//dd[@class="job_request"]/p/span[2]/text()')
                     # Job_experience = list_page_node.xpath('//dd[@class="job_request"]/p/span[3]/text()')
                     # Job_education = list_page_node.xpath('//dd[@class="job_request"]/p/span[4]/text()')
                     # Job_type = list_page_node.xpath('//dd[@class="job_request"]/p/span[5]/text()')
                     # Company_name = list_page_node.xpath('//div[@class="company"]/text()')
                     # Job_welfare = list_page_node.xpath('//dd[@class="job-advantage"]/p/text()')
                     # Job_task_request = list_page_node.xpath('//dl[@id="job_detail"]/dd[@class="job_bt"]/div/p/text()')


if __name__ == '__main__':
    main()


