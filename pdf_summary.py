import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file.
    
    Returns:
        str: Extracted text from the PDF.
    """
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_key_information(text):
    """
    Extracts key information relevant to an investor from the text.
    
    Args:
        text (str): Text extracted from the PDF.
    
    Returns:
        dict: A dictionary containing key information.
    """
    key_info = {
        "future_growth_prospects": [],
        "key_changes_in_business": [],
        "key_triggers": [],
        "material_effects_on_earnings": [],
    }

    # Extract future growth prospects
    growth_patterns = [
        r"growth of \d+%",
        r"growth rate of \d+%",
        r"expected to grow",
        r"targeting growth",
        r"growth trajectory",
    ]
    for pattern in growth_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        key_info["future_growth_prospects"].extend(matches)

    # Extract key changes in business
    changes_patterns = [
        r"acquisition of",
        r"new customers",
        r"new technology",
        r"expansion plan",
        r"strategic partnership",
    ]
    for pattern in changes_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        key_info["key_changes_in_business"].extend(matches)

    # Extract key triggers
    triggers_patterns = [
        r"new order",
        r"new business",
        r"new product",
        r"new market",
        r"new technology",
    ]
    for pattern in triggers_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        key_info["key_triggers"].extend(matches)

    # Extract material effects on earnings
    earnings_patterns = [
        r"impact on earnings",
        r"effect on revenue",
        r"impact on profit",
        r"effect on EBITDA",
        r"impact on margins",
    ]
    for pattern in earnings_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        key_info["material_effects_on_earnings"].extend(matches)

    return key_info

def main(pdf_path):
    """
    Main function to extract and print key information from a PDF.
    
    Args:
        pdf_path (str): Path to the PDF file.
    """
    text = extract_text_from_pdf(pdf_path)
    key_info = extract_key_information(text)

    print("Future Growth Prospects:")
    for item in key_info["future_growth_prospects"]:
        print(f"- {item}")

    print("\nKey Changes in Business:")
    for item in key_info["key_changes_in_business"]:
        print(f"- {item}")

    print("\nKey Triggers:")
    for item in key_info["key_triggers"]:
        print(f"- {item}")

    print("\nMaterial Effects on Earnings:")
    for item in key_info["material_effects_on_earnings"]:
        print(f"- {item}")

if __name__ == "__main__":
    pdf_path = "SJS Transcript Call.pdf"  # Replace with the path to your PDF file
    main(pdf_path)