from pyobigram.utils import sizeof_fmt,nice_time
import datetime
import time
import os

def text_progres(index,max):
	try:
		if max<1:
			max += 1
		porcent = index / max
		porcent *= 100
		porcent = round(porcent)
		make_text = ''
		index_make = 1
		make_text += ' 【 '
		while(index_make<21):
			if porcent >= index_make * 5: make_text+='◆'
			else: make_text+='◇'
			index_make+=1
		make_text += ' 】 '
		return make_text
	except Exception as ex:
			return ''

def porcent(index,max):
    porcent = index / max
    porcent *= 100
    porcent = round(porcent)
    return porcent

def createDownloading(filename,totalBits,currentBits,speed,time,tid=''):

    msg = '《 Descargando ...》\n'
    msg += text_progres(currentBits,totalBits)+'\n'
    msg += '➣ Nombre: '+filename+'\n'
    msg += '➣ Porcentaje: '+str(porcent(currentBits,totalBits))+' %\n'
    msg += '➣ Velocidad: '+sizeof_fmt(speed)+'/s\n'
    msg += '➣ Total: '+sizeof_fmt(totalBits)+'\n'
    msg += '➣ Descargado: '+sizeof_fmt(currentBits)+'\n'
    msg += '➣ Tiempo: '+str(datetime.timedelta(seconds=int(time)))+'s\n'
    if tid!='':
        msg+= '➣ /cancel_' + tid + "\n\n"
    return msg
def createUploading(filename,totalBits,currentBits,speed,time,originalname=''):
    
    msg =  '《 Subiendo ...》\n'
    msg += text_progres(currentBits,totalBits)+'\n'
    msg += '➣ Nombre: '+filename+'\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= '➣ Parte: ' + str(filename)+'\n'
    msg += '➣ Porcentaje: '+str(porcent(currentBits,totalBits))+'%\n'
    msg += '➣ Velocidad: '+sizeof_fmt(speed)+'/s\n'
    msg += '➣ Total: '+sizeof_fmt(totalBits)+'\n'
    msg += '➣ Subido: '+sizeof_fmt(currentBits)+'\n'
    msg += '➣ Tiempo: '+str(datetime.timedelta(seconds=int(time)))+'s\n\n'
    return msg
def createCompresing(filename,filesize,splitsize):
    msg = '《 Comprimiendo ...》\n'
    msg+= '➣ Nombre: ' + str(filename)+'\n'
    msg+= '➣ Tamaño Total: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= '➣ Tamaño de las Partes: ' + str(sizeof_fmt(splitsize))+'\n'
    msg+= '➣ Cantidad de Partes: ' + str(round(int(filesize/splitsize)+1,1))+'\n\n'
    return msg
def createFinishUploading(filename,filesize,split_size,current,count,findex):
    msg = '《 Subida exitosa 》\n'
    msg+= '➣ Nombre: ' + str(filename)+'\n'
    msg+= '➣ Total: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= '➣ Borrar: ' + '/del_'+str(findex)
    return msg

def createFileMsg(filename,files):
    import urllib
    if len(files)>0:
        msg= '<b>☟ Aqui estan sus Links y TxT ☟</b>\n'
        for f in files:
            url = urllib.parse.unquote(f['directurl'],encoding='utf-8', errors='replace')
            #msg+= '<a href="'+f['url']+'">🔗' + f['name'] + '🔗</a>'
            msg+= "<a href='"+url+"'>🔗"+f['name']+'🔗</a>\n'
        return msg
    return ''

def createFilesMsg(evfiles):
    msg = '➣ Archivos ('+str(len(evfiles))+')\n\n'
    i = 0
    for f in evfiles:
            try:
                fextarray = str(f['files'][0]['name']).split('.')
                fext = ''
                if len(fextarray)>=3:
                    fext = '.'+fextarray[-2]
                else:
                    fext = '.'+fextarray[-1]
                fname = f['name'] + fext
                msg+= '/txt_'+ str(i) + ' /del_'+ str(i) + '\n' + fname +'\n\n'
                i+=1
            except:pass
    return msg
def createStat(username,userdata,isadmin):
    from pyobigram.utils import sizeof_fmt
    msg = '➣ Configuraciones\n\n'
    msg+= '➣ Nombre: @' + str(username)+'\n'
    msg+= '➣ User: ' + str(userdata['moodle_user'])+'\n'
    msg+= '➣ Password: ' + str(userdata['moodle_password'])+'\n'
    msg+= '➣ Host: ' + str(userdata['moodle_host'])+'\n'
    if userdata['cloudtype'] == 'moodle':
        msg+= '➣ RepoID: ' + str(userdata['moodle_repo_id'])+'\n'
    #msg+= '🏷CloudType: ' + str(userdata['cloudtype'])+'\n'
    msg+= '➣ UpType: ' + str(userdata['uploadtype'])+'\n'
    if userdata['cloudtype'] == 'cloud':
        msg+= '➣ Dir: /' + str(userdata['dir'])+'\n'
    msg+= '➣ Zips : ' + sizeof_fmt(userdata['zips']*1024*1024) + '\n\n'
    msgAdmin = 'No'
    if isadmin:
        msgAdmin = 'Si'
    #msg+= '🦾Admin : ' + msgAdmin + '\n'
    proxy = 'NO'
    if userdata['proxy'] !='':
       proxy = 'SI'
    tokenize = 'NO'
    if userdata['tokenize']!=0:
       tokenize = 'SI'
    msg+= '➣ Proxy : ' + proxy + '\n'
    #msg+= '🔮Tokenize : ' + tokenize + '\n\n'
    return msg
