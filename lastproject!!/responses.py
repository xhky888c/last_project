from random import choice



def get_response(user_input:str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Estás muy callado hoy...'
    elif 'hola' in lowered:
        return '¡Hola! ¿Cómo estás?'
    elif 'bien' in lowered:
        return 'Me alegra que estes bien.'
    elif 'mal' in lowered:
        return 'Vamos, ánimo. Todo mejorará eventualmente.'
    elif 'sugerencia' in lowered: 
        return choice(['Ve a dar una caminata, te despejará la mente y respirarás aire fresco.(https://www.bbc.com/mundo/noticias-45792863)',
                       'Lee un libro o estudia algo. Siempre manten el papel como preferencia al estudiar, recuerda que las pantallas dañan las retinas de tus ojos(https://www.bbc.com/mundo/noticias-45792863)',
                       'Da un paseo en bicicleta, además de ejercitar tus musculos y corazón, le estarás haciendo un favor al medio ambiente(https://www.bbc.com/mundo/noticias-45792863)',
                       '¡Haz alguna manualidad! Siempre hay botellas plasticas o cajas de cartón dando vueltas, ¿Por qué no intentas hacer un macetero con una botella vieja?(https://www.bbc.com/mundo/noticias-45792863)'])
    elif 'info' in lowered:
        return 'Siempre hay que estar al tanto de lo que sucede en nuestro planeta y como podemos ayudar a este. Aquí hay articulos que podrían interesarte: https://www.un.org/es/climatechange/science/causes-effects-climate-change, https://www.nrdc.org/es/stories/cuales-son-causas-cambio-climatico, https://ciencia.nasa.gov/cambio-climatico/los-efectos-del-cambio-climatico/, https://news.un.org/es/story/2021/08/1495262, https://www.nationalgeographicla.com/medio-ambiente/2022/10/cambio-climatico-que-es-cuales-son-sus-causas-y-que-puedes-hacer-para-revertirlo, https://www.unep.org/es/noticias-y-reportajes/reportajes/10-maneras-en-que-puedes-ayudar-combatir-la-crisis-climatica.'
    
    elif 'chao' in lowered:
        return '¡Nos vemos!'
    else: 
        return choice(['No entiendo...',
                       '¿De qué hablas?',
                       '¿Podrías repetirlo?'])