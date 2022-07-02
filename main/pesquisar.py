from botcity.web import WebBot

def pesquisar():

    class Bot(WebBot):
        def action(self, execution=None):
        
            self.headless = False
            self.driver_path = r"C:\Users\mauro.morais\OneDrive - T2C CONSULTORIA LTDA\Documentos\Python\Projetos\extracaoSiteIBGE\uva\infra\chromedriver.exe"
        
            self.find_element(input@id=="twotabsearchtextbox").click()
        
            self.wait(3000)
    
            self.stop_browser()

        def not_found(self, label):
            print(f"Element not found: {label}")


    if __name__ == '__main__':
        Bot.main()

print('entrei')