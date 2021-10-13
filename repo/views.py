from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
import json
from django.http import JsonResponse
# Create your views here.



# @csrf_exempt
@api_view(['GET', 'POST'])
def getRepos(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        # print(request.data)
        print(request.query_params)
        print(request.data['items'])
        items = request.data['items']


        new_items = []
        for item in items:
            m ={}
            m['id'] = item['id']
            m['language'] = item['language']
            new_items.append(m)
        jItems =  [item['id'] for item in new_items if item['language'] == 'JavaScript']
        typeItems =  [item['id'] for item in new_items if item['language'] == 'TypeScript']
        phpItems =  [item['id'] for item in new_items if item['language'] == 'PHP']
        cPlusItems =  [item['id'] for item in new_items if item['language'] == 'C++']
        cItems =  [item['id'] for item in new_items if item['language'] == 'C']
        cSharpItems =  [item['id'] for item in new_items if item['language'] == 'C#']
        pythonItems =  [item['id'] for item in new_items if item['language'] == 'Python']
        rustItems =  [item['id'] for item in new_items if item['language'] == 'Rust']
        shellItems =  [item['id'] for item in new_items if item['language'] == 'Shell']
        javaItems =  [item['id'] for item in new_items if item['language'] == 'Java']
        rubyItems =  [item['id'] for item in new_items if item['language'] == 'Ruby']
        htmlItems =  [item['id'] for item in new_items if item['language'] == 'HTML']
        kotlinItems =  [item['id'] for item in new_items if item['language'] == 'Kotlin']
        goItems =  [item['id'] for item in new_items if item['language'] == 'Go']
        jnItems =  [item['id'] for item in new_items if item['language'] == 'Jupyter Notebook']
        cssItems =  [item['id'] for item in new_items if item['language'] == 'CSS']
        swiftItems =  [item['id'] for item in new_items if item['language'] == 'Swift']
        ocItems =  [item['id'] for item in new_items if item['language'] == 'Objective-C']
        elmItems =  [item['id'] for item in new_items if item['language'] == 'Elm']
        ocPlusItems =  [item['id'] for item in new_items if item['language'] == 'Objective-C++']
        valaItems =  [item['id'] for item in new_items if item['language'] == 'Vala']
        vsItems =  [item['id'] for item in new_items if item['language'] == 'Vim Script']
        pugItems =  [item['id'] for item in new_items if item['language'] == 'Pug']
        groovyItems =  [item['id'] for item in new_items if item['language'] == 'Groovy']
        psItems =  [item['id'] for item in new_items if item['language'] == 'PowerShell']
        hclItems =  [item['id'] for item in new_items if item['language'] == 'HCL']
        vueItems =  [item['id'] for item in new_items if item['language'] == 'Vue']
        mfItems =  [item['id'] for item in new_items if item['language'] == 'Makefile']
        scalaItems =  [item['id'] for item in new_items if item['language'] == 'Scala']
        reactItems =  [item['id'] for item in new_items if item['language'] == 'React']

        # jItems =  [item['id'] for item in new_items if item['language'] == 'JavaScript']

        # TItems = filter(lambda d:d['language']=='TypeScript', new_items)
        return Response(
            {
                'javascript': json.dumps(jItems),
                'typescript': json.dumps(typeItems),
                'c': json.dumps(cItems),
                'c++': json.dumps(cPlusItems),
                'c#': json.dumps(cSharpItems),
                'php': json.dumps(phpItems),
                'python': json.dumps(pythonItems),
                'shell': json.dumps(shellItems),
                'java': json.dumps(javaItems),
                'rust': json.dumps(rustItems),
                'ruby': json.dumps(rubyItems),
                'html': json.dumps(htmlItems),
                'kotlin': json.dumps(kotlinItems),
                'go': json.dumps(goItems),
                'jupyternotebook': json.dumps(jnItems),
                'css': json.dumps(cssItems),
                'swift': json.dumps(swiftItems),
                'objectivec': json.dumps(ocItems),
                'elm': json.dumps(elmItems),
                'objectivecplus': json.dumps(ocPlusItems),
                'vala': json.dumps(valaItems),
                'vim': json.dumps(vsItems),
                'pug': json.dumps(pugItems),
                'groovy': json.dumps(groovyItems),
                'powershell': json.dumps(psItems),
                'hcl': json.dumps(hclItems),
                'vue': json.dumps(vueItems),
                'makefile': json.dumps(mfItems),
                'scala': json.dumps(scalaItems),
                'react': json.dumps(reactItems),


            }
        )
@csrf_exempt
def postRepos(request):
    data  = json.loads(request.body.decode("utf-8"))
    print(data['total_count'])
    print(len(list(data.items())))
    # print(data['items'])
    print(len(data['items']))
    items = data['items']
    new_items = []
    for item in items:
        m ={}
        m['id'] = item['id']
        m['language'] = item['language']
        new_items.append(m)
    jItems =  [item for item in new_items if item['language'] == 'JavaScript']
    TItems = filter(lambda d:d['language']=='TypeScript', new_items)
    print(new_items)
    # print(items[0].keys())
    print(type(data['items'][0]))
    # print((list(data.items()))[1]
    print(jItems)
    print(list(TItems))
    return JsonResponse(json.dumps(jItems), status=201, safe=False)
@csrf_exempt
def welcome(request):
    return render(request, 'repo/welcome.html')