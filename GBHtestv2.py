import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver import ActionChains

@pytest.fixture(scope="module")
def driver():
    print ("Initializing Test")
    url="http://gbh.com.do/"
    driver = webdriver.Firefox()
    driver.get(url)
    yield driver
    driver.close()
#########################################################################    

@pytest.mark.parametrize("name, driver, link_location, expected", 
                                [
    
                                    ("Inicio", driver, "//li[@id='menu-item-21']", "http://gbh.com.do/"),
                                    ("Portafolio", driver, "//li[@id='menu-item-62']", "http://gbh.com.do/portafolio/"),
                                    ("Conocenos", driver, "//li[@id='menu-item-65']", "http://gbh.com.do/soluciones-gbh/"),
                                    ("Empleos", driver, "//li[@id='menu-item-126']", "http://gbh.com.do/empleos/"),
                                    ("Blog", driver, "//li[@id='menu-item-20']", "http://gbh.com.do/noticias-de-tecnologia/"),
                                 ], indirect=["driver"]
                        )
def test_links(name, driver, link_location, expected):
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, link_location)))
        
        element.click()

        driver.implicitly_wait(2)

        linkurl= driver.current_url
    except:
        linkurl = ""
    
    assert expected == linkurl
###########################################################################
    
@pytest.mark.parametrize("name, driver, dropdown_location, link_location, expected", 
                                [
    
                                    ("AsesoriaUX", driver, "//li[@id='menu-item-209']", "//li[@id='menu-item-2642']","http://gbh.com.do/servicio/desarrollo/asesoria-de-interfaz-y-experiencia-de-usuario-ui-ux/"),
                                    ("Desarrollo de Software", driver, "//li[@id='menu-item-209']", "//li[@id='menu-item-2976']","http://gbh.com.do/servicio/desarrollo/desarrollo-de-software/"),
                                    ("Diseno Paginas Web", driver, "//li[@id='menu-item-209']", "//li[@id='menu-item-226']","http://gbh.com.do/servicio/desarrollo/diseno-de-paginas-web/"),
                                    ("Manejo Redes sociales", driver, "//li[@id='menu-item-209']", "//li[@id='menu-item-2895']","http://gbh.com.do/servicio/desarrollo/manejo-de-redes-sociales-para-empresas/"),
                                    ("Consultorias Web", driver, "//li[@id='menu-item-209']", "//li[@id='menu-item-1998']","http://gbh.com.do/servicio/desarrollo/consultoria-web/"),
                                    ("SEO", driver, "//li[@id='menu-item-209']", "//li[@id='menu-item-227']","http://gbh.com.do/servicio/desarrollo/seo-optimizacion-en-motores-de-busqueda/"),
                                    ("Mantenimiento Preventivo Correctivo", driver, "//li[@id='menu-item-209']", "//li[@id='menu-item-361']","http://gbh.com.do/servicio/soporte/soporte-tecnico-mantenimiento-y-prevencion/"),
                                    ("Evaluacion Infraestructuras de IT", driver, "//li[@id='menu-item-209']", "//li[@id='menu-item-392']","http://gbh.com.do/servicio/soporte/evaluacion-de-infraestructura-de-tecnologia-de-la-informacion/"),
                                    ("Config de Respaldo", driver, "//li[@id='menu-item-209']", "//li[@id='menu-item-360']","http://gbh.com.do/servicio/soporte/configuracion-de-respaldo/"),
                                    ("Instalacion de cableado estructurado", driver, "//li[@id='menu-item-209']", "//li[@id='menu-item-357']","http://gbh.com.do/servicio/soporte/instalacion-de-cableado-estructurado/"),
                                    ("Installacion de Redes Wifi", driver, "//li[@id='menu-item-209']", "//li[@id='menu-item-358']","http://gbh.com.do/servicio/soporte/instalacion-y-configuracion-de-redes-wi-fi/"),
                                    ("Certificacion de Cableado", driver, "//li[@id='menu-item-209']", "//li[@id='menu-item-356']","http://gbh.com.do/servicio/soporte/certificacion-de-cableado-estructurado/"),
                                 ], indirect=["driver"]
                        )
def test_dropdown_links(name, driver, dropdown_location,link_location, expected):
    try:
        dropdown =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, dropdown_location)))
        
        hover = ActionChains(driver).move_to_element(dropdown)
        
        hover.perform()
        
        element = driver.find_element(By.XPATH, link_location)
        
        element.click()

        driver.implicitly_wait(2)

        linkurl= driver.current_url
    except:
        linkurl = ""
    
    assert expected == linkurl
