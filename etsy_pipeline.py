import os
import json

def create_caduceus_svg():
    # A basic SVG representation of a Caduceus
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="500" height="500">
    <!-- Staff -->
    <rect x="48" y="10" width="4" height="80" fill="#d4af37"/>
    <!-- Wings -->
    <path d="M48 30 Q20 10 10 30 Q30 40 48 35" fill="#d4af37" opacity="0.8"/>
    <path d="M52 30 Q80 10 90 30 Q70 40 52 35" fill="#d4af37" opacity="0.8"/>
    <!-- Snakes (simplified as overlapping sine waves) -->
    <path d="M40 80 Q30 70 50 60 T60 40 T50 20" fill="none" stroke="#228b22" stroke-width="3"/>
    <path d="M60 80 Q70 70 50 60 T40 40 T50 20" fill="none" stroke="#228b22" stroke-width="3"/>
    <!-- Top sphere -->
    <circle cx="50" cy="10" r="5" fill="#d4af37"/>
</svg>"""
    return svg_content

def generate_listings(listings):
    base_dir = "etsy_listings_output"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    for listing in listings:
        folder_name = listing["id"]
        folder_path = os.path.join(base_dir, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Write listing info
        with open(os.path.join(folder_path, "listing_info.txt"), "w") as f:
            f.write(f"Title: {listing['title']}\n")
            f.write(f"Price: {listing['price']}\n")
            f.write(f"Tags: {', '.join(listing['tags'])}\n")
            f.write(f"Description:\n{listing['description']}\n")

        # Write SVG image
        if listing["id"] == "caduceus_design":
            with open(os.path.join(folder_path, "design.svg"), "w") as f:
                f.write(create_caduceus_svg())

    print(f"Generated {len(listings)} listings in the '{base_dir}' folder.")

if __name__ == "__main__":
    sample_listings = [
        {
            "id": "caduceus_design",
            "title": "Medical Caduceus Symbol - Gold and Green",
            "price": "$4.99",
            "tags": ["medical", "caduceus", "nurse", "doctor", "svg file", "digital download"],
            "description": "High quality SVG file of a medical Caduceus symbol. Perfect for custom scrubs, mugs, or decals for medical professionals."
        }
    ]
    generate_listings(sample_listings)
