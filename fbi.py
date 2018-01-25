#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 15:24:28 2018

@author: credi52
"""
from random import *
import numpy as np
############################## Alphabet #############################
alph = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# On crée l'alphabet bis pour construire le checkerboard avec au moins 10 caractère supplémentaires
# au cas où le mot clé vaut dix caractères, tous unique au sein du mot clé
alph_bis = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
            "NBT", ".", ",", "É", "#", "H/M", "H/T", "À", "È", "Ê", "?", "!", "-","'"]
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
########################### Définition des lignes ###################
# Ligne A
def lineA(n):
    Ka = []
    for i in range(n):
        Ka.append(randint(0,9))
    return Ka

# Ligne B
def lineB(string):
    Kb = []
    for i in range(5):
        a = int(string[i])
        Kb.append(a)
    return Kb, int(string[5])


# Ligne C      
def lineC(Ka, Kb):
    Kc = []
    for i in range(len(Kb[0])):
        Kc.append((Ka[i]-Kb[0][i])%10)
    return Kc

# Ligne D
def lineD(string):
    Kd = []
    for i in range(20):
        Kd.append(string[i])
    return Kd

# Ligne E
def lineE(Kd):
    #Séparons Kd en deux listes de 10 caractères chacune
    Kd1 = []
    Kd2 = []
    for i in range(10):
        Kd1.append(Kd[i])
        Kd2.append(Kd[10+i])
    #Classement par ordre alphabétique
    Ke1 = Kd1
    Ke2 = Kd2
    a = 1
    b = 1
    for i in alph:
        for j in range(10):
            if i == Kd1[j]:
                Ke1[j] = a%10
                a+=1
            if i == Kd2[j]:
                Ke2[j] = b%10
                b+=1
    return Ke1, Ke2

# Ligne F
def lineF(Kc):
    Kf1 = []
    Kf2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for i in Kc:
        Kf1.append(i)
    i = 0
    while len(Kf1) < 10:
        a = (Kf1[i] + Kf1[i+1])%10
        Kf1.append(a)
        i+=1
    return Kf1, Kf2

# Ligne G
def lineG(Ke1, Kf1):
    Kg = []
    for i in range(len(Kf1)):
        Kg.append((Ke1[i]-Kf1[i])%10)
    return Kg

# Ligne H
def lineH(Ke2,Kf2,Kg):
    Kh = []
    for i in range(len(Kg)):
        Kh.append(Ke2[Kg[i-1]])
    return Kh

# Ligne J
def lineJ(Kh):
    Kj = []
    a = 1
    for i in range(10):
        Kj.append(Kh[i])
    for i in num:
        for j in range(10):
            if i == Kh[j]:
                Kj[j]=a%10
                a+=1
    return Kj
        

# Ligne K
def lineK(Kh):
    Kk = []
    for i in range(10):
        if i != 9:
            a = (Kh[i] + Kh[i+1])%10
            Kk.append(a)
        else:
            a = (Kh[i] + Kk[0])%10
            Kk.append(a)
    return Kk

# Ligne L
def lineL(Kk):
    Kl = []
    for i in range(10):
        if i != 9:
            a = (Kk[i] + Kk[i+1])%10
            Kl.append(a)
        else:
            a = (Kk[i] + Kl[0])%10
            Kl.append(a)
    return Kl

# Ligne M
def lineM(Kl):
    Km = []
    for i in range(10):
        if i != 9:
            a = (Kl[i] + Kl[i+1])%10
            Km.append(a)
        else:
            a = (Kl[i] + Km[0])%10
            Km.append(a)
    return Km

# Ligne N
def lineN(Km):
    Kn = []
    for i in range(10):
        if i != 9:
            a = (Km[i] + Km[i+1])%10
            Kn.append(a)
        else:
            a = (Km[i] + Kn[0])%10
            Kn.append(a)
    return Kn

# Ligne P
def lineP(Kn):
    Kp = []
    for i in range(10):
        if i != 9:
            a = (Kn[i] + Kn[i+1])%10
            Kp.append(a)
        else:
            a = (Kn[i] + Kp[0])%10
            Kp.append(a)
    return Kp

# Ligne QR
def lineQR(Kj, Kk, Kl, Kn, Km, Kp, parametre):
    taille_tableau_1 = parametre + Kp[7]
    taille_tableau_2 = parametre + Kp[8]
    Kstock = []
    Kq = []
    Kr = []
    for i in num:
        for j in range(10):
            if i == Kj[j]:
                Kstock.append(Kk[j])
                Kstock.append(Kl[j])
                Kstock.append(Km[j])
                Kstock.append(Kn[j])
                Kstock.append(Kp[j])
    for i in range(taille_tableau_1):
        Kq.append(Kstock[i])
    for i in range(taille_tableau_2):
        Kr.append(Kstock[taille_tableau_1+i])
    return Kq, Kr

# Ligne S
def lineS(Kp):
    Ks = []
    a = 1
    for i in range(10):
        Ks.append(Kp[i])
    for i in num:
        for j in range(10):
            if i == Kp[j]:
                Ks[j]=a%10
                a+=1
    return Ks


################################ Fonction de transformation du mot-clé ###############################
# Cette fonction prend un string et retourne un string n'ayant pas de lettre en double
def transform(mot_cle):
    L = []
    res = []
    # On transforme le mot-clé en une liste de caractère
    for i in mot_cle:
        L.append(i)
    
    # On enlève les doublons
    while len(L) != 0:
        if L[0] in res:
            L.pop(0)
        else:
            res.append(L[0])
            L.pop(0)
    return mot_cle

################################ Création du checkerboard ###############################
def checkerboard(mot_cle, Ks, chanson, date, parametre):
    n = 5
    Ka = lineA(n)
    Kb = lineB(date)
    Kc = lineC(Ka, Kb)
    Kd = lineD(chanson)
    Ke1 = lineE(Kd)[0]
    Ke2 = lineE(Kd)[1]
    Kf1 = lineF(Ke1, Ke2)[0]
    Kf2 = lineF(Ke1, Ke2)[1]
    Kg = lineG(Ke1, Kf1)
    Kh = lineH(Ke2, Kf2, Kg)
    Kj = lineJ(Kh)
    Kk = lineK(Kh)
    Kl = lineL(Kk)
    Km = lineM(Kl)
    Kn = lineN(Km)
    Kp = lineP(Kn)
    Kqr = lineQR(Kj, Kk, Kl, Kn, Km, Kp, parametre)
    Kq = Kqr[0]
    Kr = Kqr[1]
    Ks = lineS(Kp)
    
    cb = np.zeros((5, 11))
    mot_cle_bis = transform(mot_cle)
    # On remplit la première ligne avec le mot clé
    # enlève les lettres de mot_clé de alph_bis
    for i in range(10):
        if i < len(mot_cle):
            cb[1][i + 1] = mot_cle_bis[i]
            alph_bis.remove(mot_cle_bis[i])
    # On remplit colonne par colonne
    # On remplit les colonnes de 1 à 10, soit 10 colonnes
    for j in range(10):
        # On remplit les colones à partir de la 2ème ligne
        if j == 3:
            cb[2][3] = alph_bis[27-len(mot_cle_bis)]
            cb[3][3] = alph_bis[28-len(mot_cle_bis)]
            cb[4][3] = alph_bis[29-len(mot_cle_bis)]
        elif j == 5:
            cb[2][5] = alph_bis[30-len(mot_cle_bis)]
            cb[3][5] = alph_bis[31-len(mot_cle_bis)]
            cb[4][5] = alph_bis[32-len(mot_cle_bis)]
        else:
            # On remplit les ligne à partir de la ligne 2, soit 3 lignes
            for i in range(3):
                # On parcours l'alphabet sur une boucle de 3 et on ajoute les lettres au fur et à mesure.
                cb[i][j] = alph_bis[a]
                
            
            
            
    