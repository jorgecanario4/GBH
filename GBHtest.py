import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver import ActionChains

@pytest.fixture
def driver():
    url="http://gbh.com.do/"
    driver = webdriver.Firefox()
    driver.get(url)
    yield driver

def test_inicio_link(driver):
    expectedurl = "http://gbh.com.do/"
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@id='menu-item-21']")))
        
        element.click()

        driver.implicitly_wait(2)

        linkurl= driver.current_url
    except:
        linkurl = ""
    finally:
        driver.close()
    
    assert expectedurl == linkurl
    
def test_portafolio_link(driver):
    expectedurl = "http://gbh.com.do/portafolio/"
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@id='menu-item-62']")))
        
        element.click()

        driver.implicitly_wait(2)

        linkurl= driver.current_url
    except:
        linkurl = ""
    finally:
        driver.close()
    
    assert expectedurl == linkurl
    
def test_conocenos_link(driver):
    expectedurl = "http://gbh.com.do/soluciones-gbh/"
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@id='menu-item-65']")))
        
        element.click()

        driver.implicitly_wait(2)

        linkurl= driver.current_url
    except:
        linkurl = ""
    finally:
        driver.close()
    
    assert expectedurl == linkurl
    
def test_empleos_link(driver):
    expectedurl = "http://gbh.com.do/empleos/"
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@id='menu-item-126']")))
        
        element.click()

        driver.implicitly_wait(2)

        linkurl= driver.current_url
    except:
        linkurl = ""
    finally:
        driver.close()
    
    assert expectedurl == linkurl
    
def test_blog_link(driver):
    expectedurl = "http://gbh.com.do/noticias-de-tecnologia/"
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@id='menu-item-20']")))
        
        element.click()

        driver.implicitly_wait(2)

        linkurl= driver.current_url
    except:
        linkurl = ""
    finally:
        driver.close()
    
    assert expectedurl == linkurl
    
################################################################
    
def test_asesoria_N_UX_link(driver):
    expectedurl = "http://gbh.com.do/servicio/desarrollo/asesoria-de-interfaz-y-experiencia-de-usuario-ui-ux/"
    try:
        dropdown =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@id='menu-item-209']")))
        
        hover = ActionChains(driver).move_to_element(dropdown)
        
        hover.perform()
        
        element = driver.find_element(By.XPATH, "//li[@id='menu-item-2642']")
        
        element.click()

        driver.implicitly_wait(2)

        linkurl= driver.current_url
    except:
        linkurl = ""
    finally:
        driver.close()
    
    assert expectedurl == linkurl

def test_desarrollo_software_link(driver):
    expectedurl = "http://gbh.com.do/servicio/desarrollo/desarrollo-de-software/"
    try:
        dropdown =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@id='menu-item-209']")))
        
        hover = ActionChains(driver).move_to_element(dropdown)
        
        hover.perform()
        
        element = driver.find_element(By.XPATH, "//li[@id='menu-item-2976']")
        
        element.click()

        driver.implicitly_wait(2)

        linkurl= driver.current_url
    except:
        linkurl = ""
    finally:
        driver.close()
    
    assert expectedurl == linkurl


def test_diseno_pag_web_link(driver):
    expectedurl = "http://gbh.com.do/servicio/desarrollo/diseno-de-paginas-web/"
    try:
        dropdown =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@id='menu-item-209']")))
        
        hover = ActionChains(driver).move_to_element(dropdown)
        
        hover.perform()
        
        element = driver.find_element(By.XPATH, "//li[@id='menu-item-226']")
        
        element.click()

        driver.implicitly_wait(2)

        linkurl= driver.current_url
    except:
        linkurl = ""
    finally:
        driver.close()
    
    assert expectedurl == linkurl
    
def test_manejo_social_media_link(driver):
    expectedurl = "http://gbh.com.do/servicio/desarrollo/manejo-de-redes-sociales-para-empresas/"
    try:
        dropdown =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@id='menu-item-209']")))
        
        hover = ActionChains(driver).move_to_element(dropdown)
        
        hover.perform()
        
        element = driver.find_element(By.XPATH, "//li[@id='menu-item-2895']")
        
        element.click()

        driver.implicitly_wait(2)

        linkurl= driver.current_url
    except:
        linkurl = ""
    finally:
        driver.close()
    
    assert expectedurl == linkurl

def test_consultoria_web_link(driver):
    expectedurl = "http://gbh.com.do/servicio/desarrollo/consultoria-web/"
    try:
        dropdown =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@id='menu-item-209']")))
        
        hover = ActionChains(driver).move_to_element(dropdown)
        
        hover.perform()
        
        element = driver.find_element(By.XPATH, "//li[@id='menu-item-1998']")
        
        element.click()

        driver.implicitly_wait(2)

        linkurl= driver.current_url
    except:
        linkurl = ""
    finally:
        driver.close()
    
    assert expectedurl == linkurl   
    
def test_seo_link(driver):
    expectedurl = "http://gbh.com.do/servicio/desarrollo/seo-optimizacion-en-motores-de-busqueda/"
    try:
        dropdown =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@id='menu-item-209']")))
        
        hover = ActionChains(driver).move_to_element(dropdown)
        
        hover.perform()
        
        element = driver.find_element(By.XPATH, "//li[@id='menu-item-227']")
        
        element.click()

        driver.implicitly_wait(2)

        linkurl= driver.current_url
    except:
        linkurl = ""
    finally:
        driver.close()
    
    assert expectedurl == linkurl
    
def test_mantenimiento_preventivo_correctivo_links(driver):
    expectedurl = "http://gbh.com.do/servicio/soporte/soporte-tecnico-mantenimiento-y-prevencion/"
    try:
        dropdown =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@id='menu-item-209']")))
        
        hover = ActionChains(driver).move_to_element(dropdown)
        
        hover.perform()
        
        element = driver.find_element(By.XPATH, "//li[@id='menu-item-361']")
        
        element.click()

        driver.implicitly_wait(2)

        linkurl= driver.current_url
    except:
        linkurl = ""
    finally:
        driver.close()
    
    assert expectedurl == linkurl
    
def test_eval_infraestructura_IT_links(driver):
    expectedurl = "http://gbh.com.do/servicio/soporte/evaluacion-de-infraestructura-de-tecnologia-de-la-informacion/"
    try:
        dropdown =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@id='menu-item-209']")))
        
        hover = ActionChains(driver).move_to_element(dropdown)
        
        hover.perform()
        
        element = driver.find_element(By.XPATH, "//li[@id='menu-item-392']")
        
        element.click()

        driver.implicitly_wait(2)

        linkurl= driver.current_url
    except:
        linkurl = ""
    finally:
        driver.close()
    
    assert expectedurl == linkurl
    
def test_config_respaldo_links(driver):
    expectedurl = "http://gbh.com.do/servicio/soporte/configuracion-de-respaldo/"
    try:
        dropdown =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@id='menu-item-209']")))
        
        hover = ActionChains(driver).move_to_element(dropdown)
        
        hover.perform()
        
        element = driver.find_element(By.XPATH, "//li[@id='menu-item-360']")
        
        element.click()

        driver.implicitly_wait(2)

        linkurl= driver.current_url
    except:
        linkurl = ""
    finally:
        driver.close()
    
    assert expectedurl == linkurl  
    
def test_install_cableado_links(driver):
    expectedurl = "http://gbh.com.do/servicio/soporte/instalacion-de-cableado-estructurado/"
    try:
        dropdown =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@id='menu-item-209']")))
        
        hover = ActionChains(driver).move_to_element(dropdown)
        
        hover.perform()
        
        element = driver.find_element(By.XPATH, "//li[@id='menu-item-357']")
        
        element.click()

        driver.implicitly_wait(2)

        linkurl= driver.current_url
    except:
        linkurl = ""
    finally:
        driver.close()
    
    assert expectedurl == linkurl
    
def test_install_redes_wifi(driver):
    expectedurl = "http://gbh.com.do/servicio/soporte/instalacion-y-configuracion-de-redes-wi-fi/"
    try:
        dropdown =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@id='menu-item-209']")))
        
        hover = ActionChains(driver).move_to_element(dropdown)
        
        hover.perform()
        
        element = driver.find_element(By.XPATH, "//li[@id='menu-item-358']")
        
        element.click()

        driver.implicitly_wait(2)

        linkurl= driver.current_url
    except:
        linkurl = ""
    finally:
        driver.close()
    
    assert expectedurl == linkurl  
    
def test_certificacion_cableado(driver):
    expectedurl = "http://gbh.com.do/servicio/soporte/certificacion-de-cableado-estructurado/"
    try:
        dropdown =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@id='menu-item-209']")))
        
        hover = ActionChains(driver).move_to_element(dropdown)
        
        hover.perform()
        
        element = driver.find_element(By.XPATH, "//li[@id='menu-item-356']")
        
        element.click()

        driver.implicitly_wait(2)

        linkurl= driver.current_url
    except:
        linkurl = ""
    finally:
        driver.close()
    
    assert expectedurl == linkurl