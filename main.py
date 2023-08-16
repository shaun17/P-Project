import pandas
import numpy as np

chicken_original = ["Turkey (with ground bone)", "Turkey Liver", "Organic Squash", "Organic Carrots", "Organic Kale",
           "Organic Apples", "Organic Pumpkin Seeds", "Organic Sunflower Seeds", "Organic Parsley",
           "Organic Sunflower Oil", "Organic Broccoli", "Organic Blueberries", "Organic Cranberries",
           "Organic Apple Cider Vinegar", "Dried Yeast", "Montmorillonite Clay", "Fish Oil", "Organic Coconut Oil",
           "Salt", "Cod Liver Oil", "Taurine", "Organic Rosemary Extract", "Vitamin E Supplement",
           "Liquid Lactobacillus acidophilus fermentation product", "Liquid Lactobacillus casei fermentation product",
           "Liquid Lactobacillus reuteri fermentation product", "Liquid Bifidobacterium animalis fermentation product",
           "Organic Ground Alfalfa", "Dried Organic Kelp"]

pork_original = ["Pork Hearts", "Ground Pork Bones", "Pork Livers", "Organic Celery", "Organic Squash", "Organic Pumpkin Seeds",
        "Organic Sunflower Seeds", "Organic Cranberries", "Organic Blueberries", "Organic Kale", "Organic Cilantro",
        "Organic Ginger", "Organic Quinoa", "Organic Apple Cider Vinegar", "Fish Oil", "Montmorillonite Clay",
        "Organic Sunflower Oil", "Taurine", "Organic Coconut Oil", "Cod Liver Oil", "Vitamin E Supplement",
        "Organic Ground Alfalfa", "Dried Organic Kelp", "Organic Rosemary Extract",
        "Liquid Lactobacillus acidophilus fermentation product", "Liquid Lactobacillus casei fermentation product",
        "Liquid Lactobacillus reuteri fermentation product", "Liquid Bifidobacterium animalis fermentation product"]

sc_original = ["Salmon with ground bone", "chicken with ground bone", "chicken liver"," chicken gizzard", "pumpkin seed",
      "potassium chloride", "sodium phosphate", "choline chloride", "fenugreek seed",
      "dried Pediococcus acidilactici fermentation product", "dried Lactobacillus acidophilus fermentation product",
      "dried Bifidobacterium longum fermentation product"," dried Bacillus coagulans fermentation product", "taurine",
      "tocopherols (preservative)", "dandelion", "dried kelpr zinc proteinate", "iron proteinate",
      "vitamin A supplement", "vitamin E supplement", "niacin supplement", "copper proteinate", "riboflavin supplement",
      "sodium selenite", "d-calcium pantothenate", "biotin"," manganese proteinate", "thiamine mononitrate",
      "pyridoxine hydrochlotide,. vitamin D3 supplement", "folic acid", "vitamin B12 supplement"]

file_name = 'text.xlsx'
# chicken_original = list(map(lambda x: x.lower(), chicken_original)).sort()
# pork_original = list(map(lambda x: x.lower(), pork_original)).sort()
# sc_original = list(map(lambda x: x.lower(), sc_original)).sort()
chicken_original = sorted([s.lower() for s in chicken_original])
pork_original = sorted([s.lower() for s in pork_original])
sc_original = sorted([s.lower() for s in sc_original])


diff_chicken_from_pork = sorted(list({x for x in chicken_original if x not in pork_original}))
diff_pork_from_chicken = sorted(list({x for x in pork_original if x not in chicken_original}))
diff_chicken_from_sc = sorted(list({x for x in chicken_original if x not in sc_original}))
pandas.set_option("display.max_columns", 200)
df = pandas.concat(
    [pandas.DataFrame({"CHICKEN_ORIGINAL": chicken_original}), pandas.DataFrame({"PORK_ORIGINAL": pork_original}),
     pandas.DataFrame({"SC_ORIGINAL": sc_original}),
     pandas.DataFrame({"CHICKEN_DIFF_PORK": diff_chicken_from_pork}),
     pandas.DataFrame({"CHICKEN_DIFF_SC": diff_chicken_from_sc})], axis=1)

# df = pandas.DataFrame({"CHICKEN": chicken_original, "PORK": pork_original, "SC": sc_original})

df.to_excel(file_name, index=False)


