import re
import wikipedia


wikipedia.set_lang('en')

def WikipediaContent(data):
    try:
        content_link = wikipedia.page(data)
        content_text = content_link.content[:1000] 
        content_wiki = content_text.split('.')
      
        content_wiki = content_wiki[:5]
        
        content_results = ''
    
        for i in content_wiki:
            if not('==' in i):
                if(len((i.strip())) > 3):
                   content_results = content_results + i + '.'
            else:
                break

        content_results = re.sub('\([^()]*\)','', content_results)
        content_results = re.sub('\([^()]*\)','', content_results)
        content_results = re.sub('\{[^\{\}]*\}','', content_results)
    
        return content_results + '\n\n<b>Link to article:</b> ' + content_link.url
   
    except Exception as e:
        return
