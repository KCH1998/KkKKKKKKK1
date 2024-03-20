import streamlit as st

st.set_page_config(
    page_title="스포츠 종류",
    page_icon="C:\chat-gpt-prg\Streamlit-Album\images\신전.png"
)
st.markdown("""
<style>
img {
    max-height: 388px;
}
.streamlit-expanderContent div{
    display:flex;
    justify-content:center;
    front-size: 35px;
}
[data-testid="stExpandetToggleIcon"] {
            visibility:hidden;
}
</style>
""", unsafe_allow_html=True)
            

st.title("그리스 신들에 대해서")
st.markdown("찾고싶은 그리스 신들을 검색해보세요!!")

type_emoji_dict = {
    "축구": "⚽",
    "야구": "⚾",
    "농구": "🏀",


}
initial_Sport = [
    {
        "name": "제우스",
        "types": ["남자"],
        "image_url": "https://i.namu.wiki/i/tFjscbDd1rUZbmCJLNDlzkAyROQEUAjrHvECOLPcPjaRsfy07dqqXIEAlbtcLHHMRGxeGRDfGt0XQoC5-jQbXFUGyZS4SVzQ42jGY9XLGLj_tVl-vTZOXHdsaqe1QdVLo-jWThBovcCchVKSKL4Oc5eFr08nP0AvJy2ZrzjmX8o.webp"
    },
    {
        "name": "헤라",
        "types": ["여자"],
        "image_url": "https://i.namu.wiki/i/tFjscbDd1rUZbmCJLNDlzp9A3rwu4yWz7E8tQvjLugWzY-j945vmzuxFmmYaWf7flJCt-zBML_l4DnBDvZLkPPV3M5Pin_Ao5P3_KRkHb7-pX5GJ6h59Ee2Aqpup7Xi0MN9nC7Puj8ygsAeRWvKkbTaYqxAE1E1xaicJ3FCqTuE.webp",
    },
    {
        "name": "포세이돈",
        "types": ["남자"],
        "image_url": "https://i.namu.wiki/i/tFjscbDd1rUZbmCJLNDlzr1Q47VOWBACLx3-jUKAYHm3ceGiWQXkaz1v8P5kuUvo286HIkuWNf25uG0wIwuCKXBmJ0qMbvWIlGU89jC-a3VoXs8-xN2ZKEY5yfdko9hGgYhYDBHxOW-U-kjVvYP6S1CKLqsN1L95kiWYfmufjus.webp",
    },
    {
        "name": "하데스",
        "types": ["남자"],
        "image_url": "https://i.namu.wiki/i/tFjscbDd1rUZbmCJLNDlzoWleuOqovoVxUDavGl2IWY9GHvjXrqQj3aJmdbCK3xc2EOlo7xWvvIMrWB1MAKXs7IH-dLdPqKUvS-WoXFWBjBOfOdLvH87OMDYo95SI5YrsCA8KaFuyPI9mxGf9CdjGOG-KTFY2mS4NSycuSwlCNo.webp"
    },
    
        
]

example_Sport= {"name": "아르테미스",
    "types": ["여자"],
    "image_url": "https://i.namu.wiki/i/tFjscbDd1rUZbmCJLNDlzrgW6Ee6EVikT195szXAgvJdAMLjegar2uoa0BDka9-u4j3BtyqX5Jj2roeVm8z-yvTIUOwNewcBXyM9uv8G-aj05-BtKsOSwGqOWpYdraH5n1EEZokmwCDs2HrqbXgsJ0l1tVdob8GXtETyuImaZE8.webp"
}

if "Sport" not in st.session_state:
    st.session_state.Sport = initial_Sport

auto_complete = st.toggle("예시 데이터로 채우기")
print("page_reload, auto_complete", auto_complete)
with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(
            label="신의 이름",
            value=example_Sport["name"] if auto_complete else " "
        )
    with col2:
        types = st.multiselect(
            label="성별",
            options=list(type_emoji_dict.keys()),
            max_selections=2,
            default=example_Sport["types"] if auto_complete else []
        )
    image_url = st.text_input(
        label="신들의 image ",
        value=example_Sport["image_url"] if auto_complete else ""
        )
    submit = st.form_submit_button(label="Submit")
    if submit:
        if not name:
            st.error("신을 말해주세요")
        elif len(types) == 0:
            st.error("신들의 성별을 적어도 한개 선택해주세요.")
        else:
            st.success("신을 추가할 수 있습니다.")
            st.session_state.Sport.append({
                "name": name,
                "types": types,
                "image_url": image_url if image_url else "./image/default.png"
            })

for i in range(0, len(st.session_state.Sport), 3):
    row_Sport =st.session_state.Sport[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_Sport)):
        with cols[j]:
            Sport = row_Sport[j]
            with st.expander(label=f"**{i+j+1}. {Sport['name']}**", expanded=True):
                st.image(Sport["image_url"])
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x in Sport["types"]]
                st.subheader(" / ".join(emoji_types))
                delete_button = st.button(label="삭제", key=i+j, use_container_width=True)
                if delete_button:
                    del st.session_state.Sport[i+j]
                    st.rerun()