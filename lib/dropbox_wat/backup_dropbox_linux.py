import os, shutil

def bkup(src, dst):
    for root, dirs, files in os.walk(src):
        #print "root:",root
        
        for fname in files:
            # REMOVES ._ FROM LISTING (MAC OSX FORKS)
            if (fname[:2]!= "._" and 
                fname[:1]!= "." and
                fname.find('.ng') == -1 and 
                fname.find('.') != -1 and
                fname.find('out.3') == -1 and
                fname.find('out.8') == -1 and
                fname.find('.git') == -1 and
                fname.find('.gitignore') == -1 and                
                fname.find('.db') == -1):
                 
                srcPath = root.replace("\\", "/") + "/" + fname
                #print "src:",srcPath 
            
                dstPath = srcPath.replace(src, dst)
                #print "dst:",dstPath
                
                try:
                    mkDstDir = root.replace(src, dst).replace("\\", "/")
                    print mkDstDir
                    if not os.path.exists(mkDstDir):                    
                        os.makedirs(mkDstDir)
                    shutil.copy2(srcPath,dstPath)
                except:
                    print "Unable to copy files from", srcPath, "to", dstPath                    


bkup("/mnt/speakeasy/library/scripts", "/home/stickel/Dropbox/library/scripts")
bkup("/mnt/speakeasy/library/IT/scripts", "/home/stickel/Dropbox/library/IT/scripts")
bkup("/mnt/martini/scripts/Pulse", "/home/stickel/Dropbox/library/scripts/pyt/Deadline/Pulse")
