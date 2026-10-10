import streamlit as st
import pandas as pd
import plotly.express as px
import re

st.set_page_config(
    page_title="Dyeing Recipe Lab",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Visual theme ----------
st.markdown("""
<style>
    .stApp { background: #f5f8f7; }
    [data-testid="stSidebar"] { background: #112b30; }
    [data-testid="stSidebar"] * { color: #f3f8f7 !important; }
    .hero {
        padding: 1.7rem 1.9rem; border-radius: 20px;
        background: linear-gradient(120deg, #112b30, #1e5554);
        color: white; margin-bottom: 1.2rem;
    }
    .hero h1 { color: white; margin: 0 0 .45rem 0; }
    .hero p { color: #dcebe7; margin: 0; }
    .swatch {
        border: 1px solid #d8e4df; border-radius: 15px;
        overflow: hidden; background: white; margin-bottom: 10px;
    }
    .swatch-color { height: 115px; }
    .swatch-info { padding: 11px 13px; }
    .note {
        padding: .9rem 1rem; border-left: 4px solid #e59b45;
        background: #fff8ed; border-radius: 8px; color: #594a34;
    }
    div[data-testid="stMetric"] {
        background: white; border: 1px solid #dce7e3;
        padding: 14px 16px; border-radius: 14px;
    }
</style>
""", unsafe_allow_html=True)


def rgb_to_hex(r, g, b):
    return f"#{int(r):02X}{int(g):02X}{int(b):02X}"


def parse_hex(value):
    """Return an RGB tuple for a valid #RRGGBB colour, else None."""
    if not isinstance(value, str):
        return None
    value = value.strip()
    if not re.fullmatch(r"#[0-9a-fA-F]{6}", value):
        return None
    return tuple(int(value[i:i + 2], 16) for i in (1, 3, 5))


def show_swatch(name, hex_value, rgb):
    st.markdown(
        f"""
        <div class="swatch">
          <div class="swatch-color" style="background:{hex_value};"></div>
          <div class="swatch-info">
            <b>{name}</b><br>
            <code>{hex_value.upper()}</code><br>
            <span style="color:#5b706d;font-size:.86rem">RGB{rgb}</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------- Navigation ----------
with st.sidebar:
    st.markdown("## 🧪 Dyeing Recipe Lab")
    st.caption("Textile Colour & Dye Calculator")
    page = st.radio(
        "LAB MENU",
        [
            "Overview",
            "Dye Recipe Calculator",
            "RGB Colour Studio",
            "Colour Comparison",
            "Learning Corner",
        ],
    )
   
st.sidebar.markdown("---")

st.sidebar.markdown("""
<div style="
    padding: 12px;
    background-color: #1e5554;
    border: 1px solid #3b7775;
    border-radius: 10px;
    line-height: 1.7;
    color: #ffffff;
">
    <div style="font-size: 11px; color: #cde5e2;">
        PROJECT CREATED BY
    </div>
    <div style="font-size: 17px; font-weight: bold; color: #ffffff;">
        Mahreen Nawaz
    </div>
    <div style="font-size: 13px; color: #e8f4f2;">
        Roll Number: 25TE028
    </div>
</div>
""", unsafe_allow_html=True)

    



st.markdown("""
<div class="hero">
  <h1>🧪 Dyeing Recipe Lab</h1>
  <p>Calculate dye recipes, explore digital shades, and learn textile colour fundamentals.</p>
</div>
""", unsafe_allow_html=True)


# ---------- Overview ----------
if page == "Overview":
    st.subheader("Welcome to your digital textile lab")
    st.write(
        "Use the tools below to estimate dye quantities, explore RGB colours, "
        "compare shades, and understand the calculations behind a dyeing recipe."
    )
    c1, c2, c3 = st.columns(3)
    c1.metric("Recipe calculator", "Dye + liquor")
    c2.metric("RGB channels", "0–255")
    c3.metric("Colour formats", "RGB / HEX")

    st.markdown("### Lab tools")
    left, right = st.columns(2)
    with left:
        st.markdown("#### ⚖️ Dye Recipe Calculator")
        st.write("Calculate dye mass from fabric weight and concentration (% owf), plus estimated liquor volume.")
        st.markdown("#### 🎨 RGB Colour Studio")
        st.write("Adjust red, green, and blue sliders and view a live digital colour preview.")
    with right:
        st.markdown("#### 🧵 Colour Comparison")
        st.write("Compare up to three HEX colours with RGB tables and an interactive chart.")
        st.markdown("#### 📘 Learning Corner")
        st.write("Review formulas, units, examples, and the limits of digital colour matching.")

    st.markdown(
        '<div class="note"><b>Educational use:</b> Use approved laboratory recipes and safety procedures '
        'for real dyeing work. Digital RGB colours do not directly specify a physical dye recipe.</div>',
        unsafe_allow_html=True,
    )


# ---------- Dye recipe calculator ----------
elif page == "Dye Recipe Calculator":
    st.subheader("⚖️ Dye Recipe Calculator")
    st.write(
        "Enter the dry fabric weight, dye concentration as % owf "
        "(on weight of fabric), and liquor ratio."
    )

    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            fabric_kg = st.number_input(
                "Fabric weight (kg)", min_value=0.001, max_value=100000.0,
                value=1.0, step=0.1, format="%.3f"
            )
            concentration = st.number_input(
                "Dye concentration (% owf)", min_value=0.0, max_value=100.0,
                value=2.0, step=0.1, format="%.2f"
            )
        with col2:
            liquor_ratio = st.number_input(
                "Liquor ratio (1 : x)", min_value=1.0, max_value=100.0,
                value=10.0, step=0.5, format="%.1f"
            )
            water_allowance = st.number_input(
                "Additional liquor allowance (%)", min_value=0.0, max_value=100.0,
                value=0.0, step=1.0
            )

    # Dye concentration is a percentage of the dry fabric mass.
    fabric_g = fabric_kg * 1000
    dye_g = fabric_g * concentration / 100
    liquor_l = fabric_kg * liquor_ratio
    liquor_with_allowance_l = liquor_l * (1 + water_allowance / 100)

    m1, m2, m3 = st.columns(3)
    m1.metric("Required dye", f"{dye_g:,.2f} g")
    m2.metric("Estimated liquor", f"{liquor_l:,.2f} L")
    m3.metric("With allowance", f"{liquor_with_allowance_l:,.2f} L")

    st.markdown("### Calculation breakdown")
    results = pd.DataFrame([
        {"Item": "Dry fabric mass", "Formula / input": f"{fabric_kg:.3f} kg", "Calculated result": f"{fabric_g:,.2f} g fabric"},
        {"Item": "Dye mass", "Formula / input": f"{concentration:.2f}% owf", "Calculated result": f"{dye_g:,.2f} g dye"},
        {"Item": "Liquor volume", "Formula / input": f"1 : {liquor_ratio:g}", "Calculated result": f"{liquor_l:,.2f} L"},
        {"Item": "Liquor allowance", "Formula / input": f"{water_allowance:.1f}%", "Calculated result": f"{liquor_with_allowance_l:,.2f} L"},
    ])
    st.dataframe(results, use_container_width=True, hide_index=True)

    st.markdown("### Formulae")
    st.latex(r"\text{Dye (g)}=\text{Fabric (kg)}\times1000\times\frac{\text{Concentration (\% owf)}}{100}")
    st.latex(r"\text{Liquor (L, approx.)}=\text{Fabric (kg)}\times\text{Liquor ratio factor}")

    st.caption(
        "Assumption: at a 1:10 liquor ratio, use approximately 10 L of liquor per kg of fabric. "
        "Actual machine fill, process requirements, and laboratory methods can change the required volume."
    )

    st.markdown("### Multi-component recipe")
    st.write("Add dyes or chemicals and enter each component's concentration (% owf).")
    initial_recipe = pd.DataFrame({
        "Dye / chemical": ["Dye A", "Dye B", "Dye C"],
        "Concentration (% owf)": [1.0, 0.5, 0.0],
    })
    recipe = st.data_editor(
        initial_recipe,
        num_rows="dynamic",
        use_container_width=True,
        key="recipe_editor",
        column_config={
            "Dye / chemical": st.column_config.TextColumn("Dye / chemical"),
            "Concentration (% owf)": st.column_config.NumberColumn(
                "Concentration (% owf)", min_value=0.0, max_value=100.0, step=0.1
            ),
        },
    )
    if not recipe.empty:
        recipe["Concentration (% owf)"] = pd.to_numeric(
            recipe["Concentration (% owf)"], errors="coerce"
        ).fillna(0).clip(lower=0, upper=100)
        recipe["Amount (g)"] = recipe["Concentration (% owf)"] * fabric_kg * 10
        st.dataframe(recipe, use_container_width=True, hide_index=True)
        st.metric("Total listed component mass", f"{recipe['Amount (g)'].sum():,.2f} g")
        st.download_button(
            "⬇️ Download recipe CSV",
            data=recipe.to_csv(index=False).encode("utf-8"),
            file_name="dyeing_recipe.csv",
            mime="text/csv",
        )

    st.markdown(
        '<div class="note">This calculator does not determine salt, alkali, auxiliaries, '
        'temperature, pH, fixation, or dye exhaustion. Use a verified process recipe for these.</div>',
        unsafe_allow_html=True,
    )


# ---------- RGB studio ----------
elif page == "RGB Colour Studio":
    st.subheader("🎨 RGB Colour Studio")
    st.write("Move the sliders to create a digital colour. The preview and codes update automatically.")

    if "rgb_red" not in st.session_state:
        st.session_state.rgb_red = 40
        st.session_state.rgb_green = 145
        st.session_state.rgb_blue = 125

    left, right = st.columns([1, 1])
    with left:
        red = st.slider("Red", 0, 255, key="rgb_red")
        green = st.slider("Green", 0, 255, key="rgb_green")
        blue = st.slider("Blue", 0, 255, key="rgb_blue")
        hex_value = rgb_to_hex(red, green, blue)
        st.code(f"RGB({red}, {green}, {blue})\n{hex_value}", language="text")
        if st.button("Reset to teal"):
            st.session_state.rgb_red = 40
            st.session_state.rgb_green = 145
            st.session_state.rgb_blue = 125
            st.rerun()

    with right:
        st.markdown(
            f"""
            <div style="height:260px;border-radius:20px;background:{hex_value};
              border:1px solid rgba(0,0,0,.12);display:flex;align-items:end;padding:18px;">
              <div style="background:rgba(255,255,255,.92);padding:10px 14px;border-radius:10px;color:#183b3b">
                <b>Live colour preview</b><br><code>{hex_value}</code>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption("RGB/HEX values describe screen colour, not a guaranteed fabric dye formula.")

    st.markdown("### Quick shade presets")
    presets = [
        ("Deep Teal", "#287D7D"),
        ("Ocean Blue", "#246BCE"),
        ("Warm Coral", "#F07868"),
        ("Mustard", "#D6A52D"),
        ("Soft Lilac", "#B7A1D9"),
        ("Charcoal", "#30383A"),
    ]
    preset_columns = st.columns(3)
    for index, (name, value) in enumerate(presets):
        with preset_columns[index % 3]:
            show_swatch(name, value, parse_hex(value))


# ---------- Colour comparison ----------
elif page == "Colour Comparison":
    st.subheader("🧵 Colour Comparison")
    st.write("Enter HEX colours in the format #RRGGBB to compare their digital values.")

    default_values = ["#287D7D", "#F07868", "#D6A52D"]
    inputs = st.columns(3)
    colour_rows = []
    for index, col in enumerate(inputs):
        with col:
            name = f"Colour {chr(65 + index)}"
            value = st.text_input(name + " HEX", value=default_values[index], key=f"compare_hex_{index}")
            rgb = parse_hex(value)
            if rgb is None:
                st.error("Enter a valid HEX code, e.g. #287D7D.")
            else:
                show_swatch(name, value.strip().upper(), rgb)
                colour_rows.append({
                    "Colour": name,
                    "HEX": value.strip().upper(),
                    "Red": rgb[0],
                    "Green": rgb[1],
                    "Blue": rgb[2],
                })

    if colour_rows:
        colour_df = pd.DataFrame(colour_rows)
        st.markdown("### Colour values")
        st.dataframe(colour_df, use_container_width=True, hide_index=True)

        if len(colour_rows) >= 2:
            chart_data = pd.DataFrame([
                {"Colour": row["Colour"], "Channel": channel, "Value": row[channel]}
                for row in colour_rows
                for channel in ("Red", "Green", "Blue")
            ])
            fig = px.bar(
                chart_data, x="Colour", y="Value", color="Channel",
                barmode="group", range_y=[0, 255], title="RGB channel comparison",
            )
            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                yaxis_title="Channel value (0–255)",
            )
            st.plotly_chart(fig, use_container_width=True)

        st.download_button(
            "⬇️ Download colour comparison CSV",
            data=colour_df.to_csv(index=False).encode("utf-8"),
            file_name="colour_comparison.csv",
            mime="text/csv",
        )


# ---------- Learning corner ----------
elif page == "Learning Corner":
    st.subheader("📘 Learning Corner")
    st.markdown("### Key terms")
    st.markdown("""
    - **Fabric weight:** mass of the dry textile material to be dyed.
    - **% owf:** dye concentration as a percentage of dry fabric weight.
    - **Liquor ratio:** relationship between fabric mass and dye-bath liquor, often written as 1:x.
    - **RGB:** a digital colour model using red, green, and blue light.
    - **HEX:** a six-digit hexadecimal code representing a digital RGB colour.
    """)
    st.markdown("### Worked example")
    st.write("For 2 kg of fabric at 1.5% owf:")
    st.latex(r"2\times1000\times\frac{1.5}{100}=30\text{ g dye}")
    st.write("At a 1:10 liquor ratio, estimated liquor volume is 2 × 10 = 20 L.")

    st.markdown("### Remember")
    st.markdown("""
    - RGB colour values cannot be converted directly into a reliable physical dye recipe.
    - Results depend on fibre type, dye class, water quality, auxiliaries, temperature, time, pH, and finishing.
    - Verify calculations against your teacher's instructions, approved lab method, and chemical safety guidance.
    """)
    st.info("This application is a learning aid and does not replace professional dyeing instructions or safety procedures.")

st.markdown("---")
st.caption("Dyeing Recipe Lab • Streamlit + GitHub • Educational project")
