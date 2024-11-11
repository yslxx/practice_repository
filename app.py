import streamlit as st 

print('page reloaded')
st.set_page_config(
    page_title = "포켓몬 도감",
    page_icon = "./images/monsterball.png"
)

st.markdown("""
    <style>
        h1 {
            color: red;
        }
    </style>
""", unsafe_allow_html = True)


st.title("streamlit 포켓몬 도감!")

st.markdown("**포켓몬**을 하나씩 추가해서 도감을 채워보세요!")

type_emoji_dict = {
    "노말": "⚪",
    "격투": "✊",
    "비행": "🕊",
    "독": "☠️",
    "땅": "🌋",
    "바위": "🪨",
    "벌레": "🐛",
    "고스트": "👻",
    "강철": "🤖",
    "불꽃": "🔥",
    "물": "💧",
    "풀": "🍃",
    "전기": "⚡",
    "에스퍼": "🔮",
    "얼음": "❄️",
    "드래곤": "🐲",
    "악": "😈",
    "페어리": "🧚"
}

initial_pokemons = [
    {
        "name": "피카츄",
        "types": ["전기"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/pikachu.webp"
    },
    {
        "name": "누오",
        "types": ["물", "땅"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/nuo.webp",
    },
    {
        "name": "갸라도스",
        "types": ["물", "비행"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/garados.webp",
    },
    {
        "name": "개굴닌자",
        "types": ["물", "악"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/frogninja.webp"
    },
    {
        "name": "루카리오",
        "types": ["격투", "강철"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/lukario.webp"
    },
    {
        "name": "에이스번",
        "types": ["불꽃"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/acebun.webp"
    },
]

if "pokemons" not in st.session_state: # state에 pokemons라는 키 값이 있느냐
    # 없다면 
    st.session_state.pokemons = initial_pokemons # pokemons라는 이름으로 initial_pokemons를 추가한다. 
    # state는 dictiounary처럼 사용 => session state


auto_complete = st.toggle("예시 데이터로 채우기")
example_pokemon = {
    "name": "알로라 디그다",
    "types": ["땅", "강철"],
    "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/alora_digda.webp"
}

with st.form(key = "form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(label = '포켓몬 이름',
                             value = example_pokemon['name'] if auto_complete else '')
    with col2:
        types = st.multiselect(label = '포켓몬 속성', 
                            options = list(type_emoji_dict.keys()),
                            max_selections = 2,
                            default = example_pokemon['types'] if auto_complete else []) # 배열은 default, 일반 값은 value인듯. 
    image_url = st.text_input(label = '포켓몬 이미지 url')
    submit = st.form_submit_button(label = 'submit')
    if submit: # 이걸로 예외처리 가능. 비어있는 속성이 있다거나 경고메시지를 보여줄 수 있음. 
        '''
        print('name', name) # 출력은 vscode에 됨.
        print('types', types)
        print('image url', image_url) 
        '''
        if not name:
                st.error('포켓몬의 이름을 입력해주세요.')
        elif len(types) == 0:
            st.error('포켓몬의 속성을 적어도 한개 선택해주세요.')
        else:
            st.success('포켓몬을 추가할 수 있습니다.') # 메시지가 뜬거지 제출이 된게 아님
            st.session_state.pokemons.append({
                'name':name,
                'types':types,
                'image_url':image_url if image_url else "./images/default.png" # image_url이 있으면 url에 저장하고 아니면 default 이미지 지정
            })
        

for i in range(0, len(st.session_state.pokemons), 3):
    row_pokemons = st.session_state.pokemons[i:i+3]

    cols = st.columns(3)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]
            with st.expander(label = pokemon['name'], expanded = True):
                st.image(pokemon['image_url'])
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon['types']]
                st.subheader(" / ".join(emoji_types))
                delete_button = st.button(label = '삭제', key = i+j,
                                          use_container_width = True) # 지금 for문형태로 만들어지고 있는거기 때문에 button마다 key값이 모두 달라야함. 
                if delete_button:
                    print('delete button clicked!')
                    del st.session_state.pokemons[i+j]

