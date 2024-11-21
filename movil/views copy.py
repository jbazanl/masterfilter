from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate
from django.contrib.auth import logout as do_logout
from django.contrib.auth.models import User
import json
import pandas as pd
import requests
from .models import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.

def movil(request):
    print("Sesión del usuario:", request.session)
    print("Cookies recibidas:", request.COOKIES)
    print("Usuario autenticado:", request.user)
    if request.user.is_authenticated:
        #return redirect("abct")
        print(f"Username: {request.user.username}")
        print(f"Email: {request.user.email}")
        print(f"Nombre completo: {request.user.get_full_name()}")
        print(f"Último login: {request.user.last_login}")
        print(f"Fecha de registro: {request.user.date_joined}")
    
        endp = EndPoint.objects.all().first()
        perm = Permision.objects.filter(user=request.user).first()
        if not perm.movil:
            return redirect("fijo")
        doc = Document.objects.filter(user=request.user).last()
        total = 0
        name = ""
        
        #if doc:
        #    total = doc.total
        #    name = str(doc.file)
        
        # Verifica si `doc` es `None`
        if doc is not None:
            print(f"ID: {doc.id}, File: {doc.file}")
            total = doc.total
            name = str(doc.file)
        else:
            # Si no hay documentos asociados, asigna valores predeterminados
            print("No documents found for this user.")
            total = 0
            name = ""

        print(endp)
        print(total)
        print(perm.movil)
        print(name)
        return render(request, "movil.html",{
                    "segment":"movil", 
                    "subido": total, 
                    "endpoint": endp, 
                    "perm": perm, 
                    "name":name
                })
    else:
        return redirect("login")

def reanude(request):
    print("REANUDE SAM")
    doc = Document.objects.filter(user=request.user)
    for d in doc:
        if str(d.file).split("/")[1] == request.POST["file"]:
            pro_file(d, request, False)
            break
    return redirect("movil")

def upload(request):
    print("upload SAM BAZAN")
    try:
        print(request)
        print("before Document")
        print(request.user)
        doc = Document.objects.create(
            file = request.FILES["file"],
            user = request.user
        )
        pro_file(doc, request, True)
    except Exception as e:
        print(f"Se produjo una excepción: {str(e)}")
        pass
    return redirect("/")

def pro_file(doc, request, op):
    name_file = str(doc.file).split("/")[1]
    print(name_file)
    data = read_file(name_file)
    doc.save()
    send_data(request.user.username, data, op, name_file)

def read_file(name_file):
    try:
        name_file = name_file.replace(" ", "_")
        file = "media/subido/" + name_file
        df = pd.read_excel(file, sheet_name='Hoja1')
        df.describe()
        documents = df['numeros'].tolist()
        return documents
    except Exception as e:
        print(f"Error al leer el archivo: {str(e)}")
        print("Detalle del error:")
        return None

def export(request):
    print("SAM inicio funcion export en views.py")
    print("Sesión del usuario:", request.session)
    print("Cookies recibidas:", request.COOKIES)
    print("Usuario autenticado:", request.user)
    if request.user.is_authenticated:
        print("SAM user autenticado en views.py")
        data = request.POST["data"]
        #print(request.POST["data"])
        #print(request.POST["nameFile"])
        #data_all = {"number":[], "operator":[]}
        #df = pd.DataFrame()
        name_file = json.loads(data)["nameFile"]
        data = json.loads(data)["data"]["list"]
        print("SAM en views: def export request")
        print(name_file)
        file = "media/subido/" + name_file
        df = pd.read_excel(file, sheet_name='Hoja1')
        df['operador'] = pd.NA
        #print(df)
        for d in data:
            #print(d)
            df.loc[df['numeros'] == int(d['number']), 'operador'] = d["operator"]
            #data_all["operator"].append(d["operator"])
            #data_all["number"].append(d["number"])

        #df["numeros"] = data_all["number"]
        #df["operador"] = data_all["operator"]

        try:
            #df.to_excel("media/proces/"+str(request.user.username)+".xlsx")
            df.to_excel("media/proces/"+name_file)
        except Exception as e:
            print("Error: "+str(e))
        message = "Procesado correctamente"
        #return HttpResponse(json.dumps({"message": message, "file": str(request.user.username)+".xlsx", "path": "media/proces/"+str(request.user.username)+".xlsx"}))
        return HttpResponse(json.dumps({
            "message": message,
            "file": name_file, 
            #"file": str(request.user.username)+"_Movil_"+name_file+".xlsx", 
            "path": "media/proces/"+name_file
            #"path": "media/proces/"+str(request.user.username)+"_Movil_"+name_file+".xlsx"
        }))
        #return HttpResponse(json.dumps({"message": message, "file": str(request.user.username)+"_Movil_"+name_file+".xlsx", "path": "media/proces/"+str(request.user.username)+".xlsx"}))
    else:
        return redirect("login")

def send_data(user, data, op, name_file):
    try:    
        #url = "http://127.0.0.1:8800/process/"
        url = "http://185.47.131.53:8800/process/"
        #url = "https://api.masterfilter.es/process/"
        payload = json.dumps({
            "user": user,
            "number": data,
            "new":op,
            "reprocess":False,
            "file": name_file
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
    except Exception as e:
        print(f"Error al leer el archivo: {str(e)}")

def login(request):
    message = {"valid": ""}
    if request.method == "POST":
        user = request.POST["username"]
        passw = request.POST["password"]
        print(user)
        print(passw)
        Users = authenticate(username=user, password=passw)
        if Users is not None:
            do_login(request, Users)
            print("SAM auth OK")
            return redirect("movil")
        else:
            message = {"valid": "Usuario o password incorrecto"}

    return render(request, "sign-in.html", message)

def logout(request):
    do_logout(request)
    return redirect('/')