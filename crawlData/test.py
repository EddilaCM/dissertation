# __author__ = 'cm'
# -*- coding:utf-8 -*-
import returnEtree
import xlwt
import re


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
    nameArrC = ['类1','类2','类3','职位名称', '薪资', '工作地', '经验', '学历', '职位类别', '公司名称', '职位诱惑', '职位描述', '详细地址','链接','时间']
    nameArrE = ['class_one','class_two','class_three','Job_name', 'Job_salary', 'Job_area', 'Job_experience', 'Job_education', 'Job_type',
                'Company_name', 'Job_welfare', 'Job_task', 'detail_adder','link_addr','time']
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
    # print(my_big_tree)
    class1 = my_big_tree.xpath('//div[@class="menu_main job_hopping"]/div[@class="category-list"]/h2/text()')
    print(class1)
    if len(class1)!=0:
        for class1_1 in class1:
            aa = removeSpace(class1_1)
            if aa != "":
                print('class1:'+aa)
                typeOne.append(aa)
        print(len(typeOne))
        for x in range(0, len(class1), 1):
            type_big_tree = my_big_tree.xpath('//div[@class="menu_box"]')[x]
            # 一级分类
            # class_one_x_text = type_big_tree.xpath('/div[@class="menu_main job_hopping"]/div[@class="category-list"]/h2/text()')
            # class_one_x_text = removeSpace(class_one_x.text)
            class_one_x_text = typeOne[x]
            print('classOne:',class_one_x_text)
            class_twoAndthree_x = type_big_tree.xpath('div[@class="menu_sub dn"]/dl')
            print(len(class_twoAndthree_x))
            for b in class_twoAndthree_x:
                class_two = b.xpath('dt/span/text()')[0]
                print('classTwo:', class_two)
                class_three_list = b.xpath('dd/a')
                for c in class_three_list:
                    class_three = c.text
                    three_url = c.xpath('@href')[0]
                    print("url:" + three_url)
                    this_big_tee = returnEtree.header_browser(True, urlPool, three_url, User_Agent, Accept, Accept_Charset, Accept_Encoding, Host)
                    # job列表
                    total_page1 = this_big_tee.xpath('//div[@class="pager_container"]/a[(last()-1)]/text()')
                    print('yy:'+str(len(total_page1)))
                    if len(total_page1) >= 1:
                        total_page = this_big_tee.xpath('//div[@class="pager_container"]/a[(last()-1)]/text()')[0]
                        print int(total_page)
                        pre_url = three_url
                        if total_page>=1:
                            for page in xrange(1, (int(total_page)+1), 1):
                                this_url = pre_url + str(page) + '/'
                                print this_url
                                para = {'filterOption':3}
                                this_page_job_list = returnEtree.header_browser_nourl_pool(this_url, User_Agent, Accept, Accept_Charset, Accept_Encoding, Host)
                                job_link_list = this_page_job_list.xpath('//a[@class="position_link"]/@href')
                                job_times = this_page_job_list.xpath('//span[@class="format-time"]/text()')
                                for link,time in zip(job_link_list,job_times):
                                    # link = link.replace('//', '//')
                                    # wr.write(link+'\n')
                                    # m += 1
                                    print link
                                    job_sheet.write(i, 14, time)
                                    # 详细职位介绍
                                    detail_job = returnEtree.header_browser(True,urlPool,link, User_Agent, Accept, Accept_Charset, Accept_Encoding, Host)
                                    # detail_job = returnEtree.header_browser_cookie(link, User_Agent, Accept, Accept_Charset, Accept_Encoding, Host)
                                    Job_name_list = detail_job.xpath('//span[@class="name"]/text()')
                                    Job_salary = detail_job.xpath('//span[@class="salary"]/text()')
                                    Job_area = detail_job.xpath('//dd[@class="job_request"]/p/span[2]/text()')
                                    Job_experience = detail_job.xpath('//dd[@class="job_request"]/p/span[3]/text()')
                                    Job_education = detail_job.xpath('//dd[@class="job_request"]/p/span[4]/text()')
                                    Job_type = detail_job.xpath('//dd[@class="job_request"]/p/span[5]/text()')
                                    Company_name = detail_job.xpath('//div[@class="company"]/text()')
                                    Job_welfare = detail_job.xpath('//dd[@class="job-advantage"]/p/text()')
                                    Job_task_request = detail_job.xpath('//dl[@id="job_detail"]/dd[@class="job_bt"]/div/p/text()')
                                    eg = ''
                                    for p in Job_task_request:
                                        eg = eg + p
                                    Job_task = eg
                                    detail_adder1 = detail_job.xpath('//div[@class="work_addr"]/a/text()')
                                    if len(detail_adder1)!= 0:
                                        detail_adder1.pop()
                                        detail_adder = ''
                                        for d in detail_adder1:
                                            # print d
                                            detail_adder += d
                                        small_addr = detail_job.xpath('//div[@class="work_addr"]/text()')
                                        small_Str = ''
                                        for small_a in small_addr:
                                            small_Str += small_a.strip()
                                        detail_adder += small_Str
                                    else:
                                        detail_adder=''
                                    # 添加数据
                                    job_sheet.write(i, 0, class_one_x_text)
                                    job_sheet.write(i, 1, class_two)
                                    job_sheet.write(i, 2, class_three)
                                    job_sheet.write(i, 3, Job_name_list[0])
                                    job_sheet.write(i, 4, Job_salary[0])
                                    job_sheet.write(i, 5, del_dip(Job_area[0]))
                                    job_sheet.write(i, 6, del_experience(del_dip(Job_experience[0])))
                                    job_sheet.write(i, 7, del_dip(Job_education[0]))
                                    job_sheet.write(i, 8, del_dip(Job_type[0]))
                                    job_sheet.write(i, 9, del_recruit(Company_name[0]))
                                    job_sheet.write(i, 10, Job_welfare[0])
                                    job_sheet.write(i, 11, Job_task)
                                    job_sheet.write(i, 12, detail_adder)
                                    job_sheet.write(i, 13, link)
                                    i += 1
                                    JobBook.save('dataFile/laGou_JobList_all20171029_1.xls')
    else:
        print(u"没有分类1的数据")





if __name__ == '__main__':
    main()