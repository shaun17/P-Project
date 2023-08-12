chicken = ["Turkey (with ground bone)", "Turkey Liver", "Organic Squash", "Organic Carrots", "Organic Kale",
           "Organic Apples", "Organic Pumpkin Seeds", "Organic Sunflower Seeds", "Organic Parsley",
           "Organic Sunflower Oil", "Organic Broccoli", "Organic Blueberries", "Organic Cranberries",
           "Organic Apple Cider Vinegar", "Dried Yeast", "Montmorillonite Clay", "Fish Oil", "Organic Coconut Oil",
           "Salt", "Cod Liver Oil", "Taurine", "Organic Rosemary Extract", "Vitamin E Supplement",
           "Liquid Lactobacillus acidophilus fermentation product", "Liquid Lactobacillus casei fermentation product",
           "Liquid Lactobacillus reuteri fermentation product", "Liquid Bifidobacterium animalis fermentation product",
           "Organic Ground Alfalfa", "Dried Organic Kelp"]

pork = ["Pork Hearts", "Ground Pork Bones", "Pork Livers", "Organic Celery", "Organic Squash", "Organic Pumpkin Seeds",
        "Organic Sunflower Seeds", "Organic Cranberries", "Organic Blueberries", "Organic Kale", "Organic Cilantro",
        "Organic Ginger", "Organic Quinoa", "Organic Apple Cider Vinegar", "Fish Oil", "Montmorillonite Clay",
        "Organic Sunflower Oil", "Taurine", "Organic Coconut Oil", "Cod Liver Oil", "Vitamin E Supplement",
        "Organic Ground Alfalfa", "Dried Organic Kelp", "Organic Rosemary Extract",
        "Liquid Lactobacillus acidophilus fermentation product", "Liquid Lactobacillus casei fermentation product",
        "Liquid Lactobacillus reuteri fermentation product", "Liquid Bifidobacterium animalis fermentation product"]

sc = ["Salmon with ground bone", "chicken with ground bone", "chicken liver; chicken gizzard", "pumpkin seed",
      "potassium chloride", "sodium phosphate", "choline chloride", "fenugreek seed",
      "dried Pediococcus acidilactici fermentation product", "dried Lactobacillus acidophilus fermentation product",
      "dried Bifidobacterium longum fermentation product; dried Bacillus coagulans fermentation product", "taurine",
      "tocopherols (preservative)", "dandelion", "dried kelpr zinc proteinate", "iron proteinate",
      "vitamin A supplement", "vitamin E supplement", "niacin supplement", "copper proteinate", "riboflavin supplement",
      "sodium selenite", "d-calcium pantothenate", "biotin; manganese proteinate", "thiamine mononitrate",
      "pyridoxine hydrochlotide,. vitamin D3 supplement", "folic acid", "vitamin B12 supplement"]

diff_chicken_from_pork = {x for x in chicken if x not in pork}
diff_pork_from_chicken = {x for x in pork if x not in chicken}
diff_chicken_from_sc = {x for x in chicken if x not in sc}

print(diff_chicken_from_pork)
print(diff_pork_from_chicken)
print(diff_chicken_from_sc)
