interaction_db = {
    ("Warfarin", "Aspirin"): {
        "severity": "major",
        "description": "Increased risk of bleeding due to combined anticoagulant and antiplatelet effects."
    },
    ("Ibuprofen", "Lisinopril"): {
        "severity": "moderate",
        "description": "Ibuprofen may reduce the effect of Lisinopril."
    },
    ("Warfarin", "Ibuprofen"): {
        "severity": "major",
        "description": "NSAIDs can displace warfarin from protein binding sites and cause GI toxicity, increasing bleeding risk."
    },
    ("Warfarin", "Omeprazole"): {
        "severity": "moderate",
        "description": "May increase warfarin concentrations by inhibiting metabolism, potentially raising INR and bleeding risk."
    },
    ("Warfarin", "Simvastatin"): {
        "severity": "moderate",
        "description": "Inhibits warfarin metabolism via CYP2C9 pathway, potentially increasing bleeding risk."
    },
    ("Simvastatin", "Clarithromycin"): {
        "severity": "major",
        "description": "Inhibits metabolism of simvastatin, significantly increasing risk of myopathy and rhabdomyolysis."
    },
    ("Simvastatin", "Amiodarone"): {
        "severity": "moderate",
        "description": "Amiodarone inhibits CYP3A4, which may decrease statin metabolism and increase risk of muscle toxicity."
    },
    ("Methotrexate", "Ibuprofen"): {
        "severity": "major",
        "description": "NSAIDs reduce renal clearance of methotrexate by approximately 40%, potentially causing toxic accumulation."
    },
    ("Fluoxetine", "Selegiline"): {
        "severity": "major",
        "description": "Combination may cause serotonin syndrome with potentially life-threatening symptoms."
    },
    ("Levothyroxine", "Omeprazole"): {
        "severity": "moderate",
        "description": "Acid-reducing medications may decrease absorption of levothyroxine, reducing effectiveness."
    },
    ("Clopidogrel", "Omeprazole"): {
        "severity": "moderate",
        "description": "Omeprazole inhibits conversion of clopidogrel to its active form, potentially reducing antiplatelet effectiveness."
    }
}
