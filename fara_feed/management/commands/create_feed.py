# this is modified from Arron's reporting feed for the lobbying tracker in "Willard"
import datetime
import re
import sys
import time
import urllib
import urllib2
import string
import lxml.html
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand, CommandError
from optparse import make_option

from fara_feed.models import Document

def add_document(url_info):
    document = Document(url = url_info[0],
        reg_id = url_info[1],
        doc_type = url_info[2],
        stamp_date = url_info[3],
    )
    document.save()
    print "Document saved"

def parse_and_save(page):
    print "Starting parse and save"
    filings = page.find("table", {"class" : "t14Standard"})
    new_fara_docs = []
    ##new_info = []

    for l in filings.find_all("a"):
        #print "starting l loop"
        link = str(l)
        url = str(re.findall(r'href="(.*?)"', link))
        url = re.sub("\['",'', re.sub("'\]", '', url))
    
        if url[:4] == "http":
            if Document.objects.filter(url = url).exists():
                print url, " in system"
            else:    
                print "new--- ", url 
                reg_id = re.sub('-','', link[34:38])
                reg_id = re.sub('S','', reg_id)
                reg_id = re.sub('L','', reg_id)
                re.findall(r'href="(.*?)"', url)
                info = re.findall( r'-(.*?)-', url)

                if info[0] == 'Amendment':
                    doc_type = 'Amendment'
                    raw_date = None

                else:
                    raw_date = info[1]

                    if info[0] == 'Short':
                        doc_type = 'Short Form'

                    elif info[0] == 'Exhibit':
                        if "AB" in url:
                            doc_type = 'Exhibit AB'  
                        if "C" in url:
                            doc_type = 'Exhibit C'    
                        if "D" in url:
                            doc_type = 'Exhibit D'

                    elif info[0] == 'Conflict':
                        doc_type = 'Conflict Provision'

                    elif info[0] == 'Registration':
                        doc_type = 'Registration'

                    elif info[0] == 'Supplemental':
                        doc_type = 'Supplemental' 

                    else:
                        print "Can't identify form-- ", url

                if raw_date != None:
                    raw_date = raw_date[3:5] + raw_date[-2:] + raw_date[:4]
                    stamp_date = datetime.datetime.strptime(raw_date, "%M%d%Y")

                else:
                    stamp_date = raw_date

                url_info= [url, reg_id, doc_type, stamp_date]
                #saves url info
                add_document(url_info)

                new_fara_docs.append(url_info)
                print "saving", url_info
                ##new_info.append(new_fara_docs)
    print "loop"               
    return new_fara_docs

class Command(BaseCommand):
    can_import_settings = True
    #option_list = BaseCommand.option_list + (
        #make_option()) to add more console command options
        
    def handle(self, *args, **options):
        url = 'https://efile.fara.gov/pls/apex/f?p=125:10:::NO::P10_DOCTYPE:ALL'

        page = urllib2.urlopen(url).read()
        doc = lxml.html.fromstring(page)
        form = doc.cssselect('form')[0]

        data = []
        for input in form.cssselect('input'):
            if input.attrib.get('name'):
                if input.attrib['name'] in ('p_t01', 'p_t02', 'p_t06', 'p_t07', 'p_request'):
                    continue
                data.append((input.attrib['name'], input.attrib['value']))

        start_date = datetime.date(2011, 01, 01) - datetime.timedelta(9)
        #start_date = datetime.date(2011, 01, 01) - datetime.date(2013, 02, 01)
        
        print start_date
        end_date = datetime.date.today()

        data += [('p_t01', 'ALL'),
                 ('p_t02', 'ALL'),
                 ('p_t06', start_date.strftime('%m/%d/%Y')),
                 ('p_t07', end_date.strftime('%m/%d/%Y')),
                 ('p_request', 'SEARCH'),
                 ]
    
        #url = 'http://209.11.109.152/pls/htmldb/wwv_flow.accept'
        url = 'https://efile.fara.gov/pls/apex/wwv_flow.accept'

        req = urllib2.Request(url, data=urllib.urlencode(data))
        page = urllib2.urlopen(req).read()
        page = BeautifulSoup(page)
        parse_and_save(page)
    
        #looking for additional pages of results 
        url_end = page.find("a", {"class":"t14pagination"})
        count = 0 
        
        while url_end != "None":
            print "while loop"
            #### I am sure this is wrong but it works :(
            url_end = str(url_end)
            url_end = url_end.replace('&amp;', '&')
            url_end = re.sub('<a class="t14pagination" href="', '/', url_end) 
            url_end = re.sub('">Next &gt;</a>', '', url_end)
            #url_end = re.sub('>&lt;Previous</a>', '', url_end)
            next_url = 'https://efile.fara.gov/pls/apex' + url_end
            print next_url
            req = urllib2.Request(next_url)
            page = urllib2.urlopen(req).read()
            page = BeautifulSoup(page)
            new_info = parse_and_save(page)
            print " made it here "
            url_end = page.findAll("a", {"class":"t14pagination"})
            
            #for m in url_end:
            if len(url_end) > 1:
                url_end = url_end[1]
            else: 
                break   
            
            print url_end.text
          
            
            print url_end
            
            print "next round = ", url_end
            count += 1
            print count
            
            
            #new_info = parse_and_save(filings)
            #print new_info
        
        print "done!"   
        #return new_fara_docs