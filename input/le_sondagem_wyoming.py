#adaptado de https://pypi.org/project/SkewT/

from numpy import ma

class Sounding():
    def __init__(self,filename=None):
         self.soundingdata={}
         self.uwyofile(filename)    

    def uwyofile(self,fname):
        """Reads the raw profile data from a Universiy of Wyoming sounding file.
    
        This is the primary method of IO for SkewT. The University of 
        Wyoming maintains a nice database of global upper air data which is
        kept up-to-date. Given a filename, this method updates the sounding 
        data with the text data in the file.
    
        NOTES
        1. The input file has to conform *Exactly* to the University of 
           Wyoming file format. This is because I look for data fields at 
           specific places on each line.
        2. I ignore the diagnostics at the end of the file, because the idea 
           is to calculate these myself.
        3. When this no longer works I'll begin reading in a more array-esque 
           way.
        """
        #--------------------------------------------------------------------
        # This *should* be a convenient way to read a uwyo sounding
        #--------------------------------------------------------------------
        fid=open(fname)
        lines=fid.readlines()
    
        # New: handle whitespace at top of file if present
        while not lines[0].strip():
            lines.pop(0)
    
    
        nlines=len(lines)
    
        lhi=[1, 9,16,23,30,37,46,53,58,65,72]
        rhi=[7,14,21,28,35,42,49,56,63,70,77]
    
    
        # initialise output data structure
        output={}
    
        fields=lines[3].split()    
    
        # This is a data pre-initialisation step. I have used the number of lines minus the number
        # of lines of diagnostics
        for ff in fields:
            # output[ff.lower()]=zeros((nlines-34))-999.
            output[ff.lower()]=[]
    
        lcounter=5
        for line,idx in zip(lines[6:],range(nlines)):
            lcounter+=1
            ### Version < 0.1.4
            # try: output[fields[0].lower()][idx]=float(line[lhi[0]:rhi[0]])
            # except ValueError: break
    
            ### New code. We test for pressure in the first column. 
            ### If there's no pressure, we get out!
            try: 
                output[fields[0].lower()].append(float(line[lhi[0]:rhi[0]]))
            except ValueError: 
                break
            
            for ii in range(1,len(rhi)):
                try: 
                    # Debug only:
                    # print fields[ii].lower(), float(line[lhi[ii]:rhi[ii]].strip())
                    ### Version < 0.1.4
                    # output[fields[ii].lower()][idx]=float(line[lhi[ii]:rhi[ii]].strip())
                     
                    ### New Code. Append to list instead of indexing 
                    ### pre-allocated data. Explicitly allocate -999
                    ### for invalid data (catch ValueError)
                    textdata=line[lhi[ii]:rhi[ii]].strip()
                    output[fields[ii].lower()].append(float(textdata))
                except ValueError: 
                    output[fields[ii].lower()].append(-999.)
    
        for field in fields:
            ff=field.lower()
            # set mask for missing data
            dd=ma.masked_values(output[ff],-999.)
            dd=ma.masked_array(dd,mask=False)
            dd.harden_mask()
            self.soundingdata[ff]=dd
    
        return None
