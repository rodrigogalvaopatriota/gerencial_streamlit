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

    st.title("Reparo repetido") 
    # Criar duas colunas para o layout
    col1, col2 = st.columns([4, 1])  # Ajuste as proporções como preferir (3:2, 1:1, etc.)

    # Carregar os dados do arquivo Excel
    df = pd.read_excel(f'resultado_reparo_repetido.xlsx') 
    #df = df.rename(columns={'Supervisor':'Coordenador'})

    df_tecnico = pd.read_excel(f'resultado_tecnico_campo.xlsx') 
    
   
  

    # Filtro por Coordenador (status_distancia)
    
    with col1:
        #st.write("### Por Coordenador:")
        opcoes_gerente = df["Gerente"].unique()
        filtro_gerente = st.sidebar.multiselect(
            "Escolha os Coordenadore(s)",
            opcoes_gerente
                  
        )

       opcoes_uf = df["Gerente"].unique()
       filtro_gerente = st.sidebar.multiselect(
                "Escolha as uf(s)",
                opcoes_uf
                      
            )
    
        opcoes_municipio = df["Gerente"].unique()
        filtro_municipio = st.sidebar.multiselect(
                "Escolha os Município(s)",
                opcoes_municipio
                      
            )
    
   

    # Verificar se ambos os filtros possuem seleções
    if not distancias:
        st.error("Por favor, selecione pelo menos um status de distância.")
    
    
    else:
        # Filtrar os dados com base nas seleções
        data = df[
            (df["Gerente"].isin(filtro_gerente))&
            (df["uf"].isin(opcoes_uf))&
            (df["municipio"].isin(opcoes_uf))
        ]

       

     
        # Exibir gráficos e tabela
        with col1:
            st.write("### Por Gerente", width=4000)
            st.dataframe(data, width=4000)  # Define a largura da tabela

            
            
            """ 
              st.write("### Por Técnico", width=4000)
            st.markdown('<p style="font-size:20px; font-weight:bold;">Top</p>', unsafe_allow_html=True)
            #st.write("### Top", width=4000)
            st.dataframe(df_tecnico_top, width=4000)  # Define a largura da tabela
            st.markdown('<p style="font-size:20px; font-weight:bold;">Bottom</p>', unsafe_allow_html=True)
            #st.write("### Bottom", width=4000)
            st.dataframe(df_tecnico_bottom, width=4000)  # Define a largura da tabela
          
            
            
            """
          

    

except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")

