

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Simulador Projetos IP",
        page_icon=r'brasao_poli.jpg',
    )

    st.write('''# Simulador de Projetos Luminotécnicos''')

    st.sidebar.info('''
                    Meu nome é **Matheus Oliver de Carvalho Cerqueira**, 
                    e este aplicativo é parte do meu 
                    **Trabalho de Conclusão de Curso** para obtenção 
                    do título de **Engenheiro de Computação**
                    durante o semestre de **2023.2**,
                    na **Univerisdade Federal da Bahia**.''')
    st.sidebar.info('''**Orientador:**' Antônio Carlos Lopes Fernandes Junior''')
    st.sidebar.info('''**Coorientador:**' Wild Freitas da SIlva Santos''')

    # st.markdown(
    #     """
    #     Streamlit is an open-source app framework built specifically for
    #     Machine Learning and Data Science projects.
    #     **👈 Select a demo from the sidebar** to see some examples
    #     of what Streamlit can do!
    #     ### Want to learn more?
    #     - Check out [streamlit.io](https://streamlit.io)
    #     - Jump into our [documentation](https://docs.streamlit.io)
    #     - Ask a question in our [community
    #       forums](https://discuss.streamlit.io)
    #     ### See more complex demos
    #     - Use a neural net to [analyze the Udacity Self-driving Car Image
    #       Dataset](https://github.com/streamlit/demo-self-driving)
    #     - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    # """
    # )


if __name__ == "__main__":
    run()
