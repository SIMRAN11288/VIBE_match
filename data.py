import pandas as pd

def get_fashion_data():
    data=[
        {"name": "Boho Dress", "desc": "Flowy, earthy tones for festival vibes", "vibes": ["boho", "cozy"]},
        {"name": "Street Hoodie", "desc": "Bold colors, oversized fit for an energetic street look", "vibes": ["urban", "chic"]},
        {"name": "Denim Jacket", "desc": "Classic blue denim with a modern edge", "vibes": ["casual", "cool"]},
        {"name": "Linen Shirt", "desc": "Lightweight and breezy, perfect for summer days", "vibes": ["casual", "beachy"]},
        {"name": "Velvet Blazer", "desc": "Elegant deep hues with luxurious texture for formal evenings", "vibes": ["classy", "elegant"]},
        {"name": "Graphic Tee", "desc": "Pop-culture prints with a modern street vibe", "vibes": ["urban", "youthful"]},
        {"name": "Wool Sweater", "desc": "Soft texture and warm tones for cozy winter vibes", "vibes": ["cozy", "minimal"]},
        {"name": "Summer Maxi Dress", "desc": "Lightweight chiffon with floral prints, perfect for beach vacations and sunny brunches", "vibes": ["boho","beachy", "feminine"]},
        {"name": "Silk Slip Dress", "desc": "Smooth satin finish with minimalist straps for a classy evening vibe", "vibes": ["elegant", "minimal", "chic"]},
        {"name": "Knitted Sweater Dress", "desc": "Cozy wool knit with warm tones, perfect for autumn walks and coffee dates", "vibes": ["cozy", "warm", "casual"]},
        {"name": "Ruffled Midi Dress", "desc": "Playful ruffles and soft pastel shades give a charming and romantic look","vibes": ["romantic", "feminine", "soft"]},

    ]
    df=pd.DataFrame(data)
    return df