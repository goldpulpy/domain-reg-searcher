import whois


class DomainSearcher:
    def __init__(self):
        self.wordlist = []
        self.domain_list = []
        self.tld_list = []




#Add single world
    def AddWord(self, word):
        word = self.ClearWord(word)
        self.wordlist.append(word)
        return word
#Load file of worlds
    def AddWordFile(self, wordfile):
        counts = 0
        with open(wordfile, "r") as f:
            for line in f:
                line = self.ClearWord(line)
                self.wordlist.append(line)
                counts += 1
        return counts

#Return world list
    def GetWordList(self):
        return self.wordlist


#---------------------------------------------

#Add TLD
    def AddTLD(self, tld):
        tld = self.ClearWord(tld)
        tld = tld.strip(".")
        self.tld_list.append(tld)
        return tld

#Load file of TLD   
    def AddTLDFile(self, tldfile):
        counts = 0
        with open(tldfile, "r") as f:
            for line in f:
                line = self.ClearWord(line)
                line = line.strip(".")
                self.tld_list.append(line)
                counts += 1
        return counts

#Return TLD list
    def GetTLDList(self):
        return self.tld_list

#---------------------------------------------


#Add domain 
    def AddDomain(self, domain):
        domain = self.ClearWord(domain)
        self.domain_list.append(domain)
        return domain
    
    def AddDomainFile(self, domainfile):
        counts = 0
        with open(domainfile, "r") as f:
            for line in f:
                line = self.ClearWord(line)
                self.domain_list.append(line)
                counts += 1
        return counts

#---------------------------------------------
#Generate domain name
    def Generate(self, method):
        counts = 0

        if method == 1:
            for i in range(len(self.wordlist)):
                self.domain_list.append(self.wordlist[i])
                counts += 1
        elif method == 2:
            for i in range(len(self.wordlist)):
                for j in range(len(self.wordlist)):
                    self.domain_list.append(self.wordlist[i] + self.wordlist[j])
                    counts += 1

        elif method == 3:
            for i in range(len(self.wordlist)):
                for j in range(len(self.wordlist)):
                    for k in range(len(self.wordlist)):
                        self.domain_list.append(self.wordlist[i] + self.wordlist[j] + self.wordlist[k])
                        counts += 1

        elif method == 4:
            for i in range(len(self.wordlist)):
                for j in range(len(self.wordlist)):
                    for k in range(len(self.wordlist)):
                        for l in range(len(self.wordlist)):
                            self.domain_list.append(self.wordlist[i] + self.wordlist[j] + self.wordlist[k] + self.wordlist[l])
                            counts += 1
        


        return counts

    def GetDomainList(self):
        return self.domain_list




    def ClearWord(self, word):
        word = word.lower()
        word = word.strip("\n")
        word = word.replace("_", "");word = word.replace("@", "");word = word.replace("~", "")
        word = word.replace("!", "");word = word.replace("#", "");word = word.replace("%", "")
        word = word.replace("^", "");word = word.replace("&", "");word = word.replace("*", "")
        word = word.replace("(", "");word = word.replace(")", "");word = word.replace("+", "")
        word = word.replace("=", "");word = word.replace("{", "");word = word.replace("}", "")
        word = word.replace("[", "");word = word.replace("]", "");word = word.replace("|", "")
        word = word.replace(";", "");word = word.replace("<", "");word = word.replace(">", "")
        word = word.replace(":", "");word = word.replace(",", "");word = word.replace("/", "");

        return word




#Check domains and return list
    def CheckDomain(self, domain, tld):
        try:
            if whois.whois(f"{domain}.{tld}")["domain_name"] == None: 
                return True
            else: return False
        except whois.parser.PywhoisError:
            return True
        
