import streamlit as st

# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(
    page_title="特定商取引法に基づく表記",
    layout="centered"
)

# -------------------------------------------------
# Style (Black background, White & Orange)
# -------------------------------------------------
st.markdown(
    """
    <style>
    body {
        background-color: #000000;
        color: #FFFFFF;
    }

    .block-container {
        max-width: 720px;
        padding-top: 4rem;
        padding-bottom: 4rem;
    }

    h1, h2, h3, p, li, div {
        color: #FFFFFF;
    }

    a {
        color: #FF8C00 !important;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# Content
# -------------------------------------------------
st.title("特定商取引法に基づく表記")

st.markdown(
    """
**販売事業者名**  
合同会社225NOW  

**運営責任者**  
阿佐 悠平  

**所在地**  
東京都墨田区太平3丁目12番9号  

**電話番号**  
請求があった場合には、遅滞なく開示いたします。  

**メールアドレス**  
225now.yaho@gmail.com  

**販売価格**  
月額プラン：USD 700  
年額プラン：USD 5,000  

**商品代金以外の必要料金**  
なし  

**支払方法**  
クレジットカード決済（Stripe）  

**支払時期**  
申込み時に即時決済  

**商品の提供時期**  
決済完了後、即時利用可能  

**返品・キャンセルについて**  
デジタルコンテンツの性質上、  
原則として返品・返金には応じておりません。  

**表現および商品に関する注意書き**  
本サービスは投資助言を目的としたものではありません。  
特定の金融商品、投資手法、または投資成果を保証するものではありません。
"""
)

st.markdown("---")

# Homeリンク（ここが重要）
st.markdown("[← Back to Home](/)")
