import streamlit as st
from PIL import Image
import random
from img_utils import load_and_split, assemble
from state import PuzzleState, GOAL_STATE
from search_utils import a_star

st.set_page_config(layout="centered")
st.title("🧩 8-Puzzle Solver with A★ Search")
st.markdown("""
Upload any image and see it transformed into a classic 8-puzzle game.
- Shuffle it
- Solve it with A★
- Visualize each step
""")

uploaded_file = st.file_uploader("1. Upload your image (JPG or PNG)", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    tiles = load_and_split(image, size=300)

    st.markdown("### Image split into 9 tiles:")
    cols = st.columns(3)
    for i in range(9):
        with cols[i % 3]:
            st.image(tiles[i], use_column_width=True)

    if st.button("2. Shuffle Puzzle"):
        while True:
            perm = list(range(9))
            random.shuffle(perm)
            if PuzzleState.is_solvable(perm) and tuple(perm) != GOAL_STATE:
                break
        start_state = PuzzleState(tuple(perm))
        st.session_state["start_state"] = start_state

    if "start_state" in st.session_state:
        st.markdown("### Shuffled Puzzle:")
        board = st.session_state["start_state"].board
        shuffled_img = assemble(board, tiles)
        st.image(shuffled_img, caption="Puzzle to be solved", use_column_width=False)

        if st.button("3. Solve with A★"):
            with st.spinner("Solving..."):
                result = a_star(st.session_state["start_state"])

            if result["success"]:
                st.success(f"Solved in {len(result['path']) - 1} moves!")
                st.info(f"Nodes explored: {result['nodes_expanded']}, Time: {result['time']:.3f}s")
                st.markdown("### Solution Steps:")
                for i, state in enumerate(result["path"]):
                    st.write(f"Step {i}:")
                    step_img = assemble(state.board, tiles)
                    st.image(step_img, width=200)
            else:
                st.error("No solution found.")
