import pandas as pd
from datetime import datetime
import streamlit as st
import altair as alt


try:
    st.set_page_config(layout="wide")

    # Adicionar uma imagem no topo da página
    st.image(
        "ico.jpg",  # Caminho para a imagem
        width=100,
        use_container_width=False,
     
    )

    st.title("Produtividade") 
    # Criar duas colunas para o layout
    col1, col2 = st.columns([4, 1])  # Ajuste as proporções como preferir (3:2, 1:1, etc.)

    # Carregar os dados do arquivo Excel
    df = pd.read_excel(f'resultado_coordenador_campo.xlsx') 
    df = df.rename(columns={'Supervisor':'Coordenador'})

    df_tecnico = pd.read_excel(f'resultado_tecnico_campo.xlsx') 
    df_tecnico_top = df_tecnico.head(10)
    df_tecnico_bottom = df_tecnico.tail(10)
   
  

    # Filtro por Coordenador (status_distancia)
    with col1:
        #st.write("### Por Coordenador:")
        distancias = st.multiselect(
            "Escolha os Coordenadores",
            df["Coordenador"].unique(),
            default=df["Coordenador"].unique()  # Seleciona todos os status por padrão
            
        )
    
   

    # Verificar se ambos os filtros possuem seleções
    if not distancias:
        st.error("Por favor, selecione pelo menos um status de distância.")
    
    
    else:
        # Filtrar os dados com base nas seleções
        data = df[
            (df["Coordenador"].isin(distancias)) 
            #(df["nome_coordenador"].isin(coordenadores))
        ]

       

     
        # Exibir gráficos e tabela
        with col1:
            st.write("### Por Coordenador", width=4000)
            st.dataframe(data, width=4000)  # Define a largura da tabela

            st.write("### Por Técnico", width=4000)
            st.markdown('<p style="font-size:20px; font-weight:bold;">Top</p>', unsafe_allow_html=True)
            #st.write("### Top", width=4000)
            st.dataframe(df_tecnico_top, width=4000)  # Define a largura da tabela
            st.markdown('<p style="font-size:20px; font-weight:bold;">Bottom</p>', unsafe_allow_html=True)
            #st.write("### Bottom", width=4000)
            st.dataframe(df_tecnico_bottom, width=4000)  # Define a largura da tabela
          

    

except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")
