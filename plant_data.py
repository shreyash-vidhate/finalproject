from app import db, Plant, Disease, app

def insert_data():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Add data for existing and new plants in alphabetical order
        plants = [
            'Apple', 'Grapes', 'Mango', 'Onion', 'Potato', 'Rose', 'Sugarcane', 'Tomato', 'Wheat'
        ]

        for plant_name in plants:
            plant = Plant(name=plant_name)
            db.session.add(plant)
        db.session.commit()

        # Add disease data for Apple at the seeding stage
        apple = Plant.query.filter_by(name='Apple').first()
        apple_diseases_seeding = [
            ('Anthracnose of Apple',
            '''Symptoms:<br>
            - Dark, sunken lesions on leaves and fruit, which may expand and coalesce.<br>
            - Premature leaf drop, leading to reduced photosynthesis.<br>
            - Fruit may develop dark spots and rot, making them unmarketable.<br>
            <br>
            Causes:<br>
            - Caused by the fungal pathogen (Colletotrichum spp.) that thrives in warm, wet conditions, especially during periods of high humidity.<br>
            <br>
            Preventive Measures:<br>
            - Ensure good air circulation around plants by proper spacing.<br>
            - Avoid overhead watering to reduce humidity on foliage.<br>
            - Remove and destroy infected plant debris at the end of the season.<br>
            - Apply fungicides as a preventive measure during wet seasons, especially before flowering.<br>
            <br>
            Treatment:<br>
            - If infection occurs, apply fungicides labeled for anthracnose control, following the manufacturer's instructions.''','Seeding'
        ),
        (
            'Apple Mosaic Virus',
            '''Symptoms:<br>
            - Yellowing and mottling of leaves, which may appear as light and dark green patches.<br>
            - Stunted growth and reduced fruit yield, affecting overall plant vigor.<br>
            - Leaves may curl or become distorted, impacting photosynthesis.<br>
            <br>
            Causes:<br>
            - Viral infection transmitted by aphids and other sap-sucking insects, which can spread the virus from infected to healthy plants.<br>
            <br>
            Preventive Measures:<br>
            - Control aphid populations with insecticidal soap or neem oil to reduce transmission risk.<br>
            - Remove and destroy infected plants to prevent further spread.<br>
            - Use virus-resistant apple varieties when available to minimize risk.<br>
            <br>
            Treatment:<br>
            - There is no cure for viral infections; focus on prevention and management of aphid populations.''','seeding'
        ),
        (
            'Stecklenberger Disease',
            '''Symptoms:<br>
            - Leaf spots that may coalesce into larger areas, leading to significant leaf loss.<br>
            - Yellowing of leaves and premature leaf drop, which can reduce fruit quality.<br>
            - Reduced fruit quality and yield, with potential for fruit drop.<br>
            <br>
            Causes:<br>
            - Caused by the fungal pathogen (Mycosphaerella pomi) that spreads in wet conditions, particularly during rainy seasons.<br>
            <br>
            Preventive Measures:<br>
            - Prune trees to improve air circulation and reduce humidity around foliage.<br>
            - Apply fungicides during the growing season, especially during wet weather.<br>
            - Remove fallen leaves and debris to reduce fungal spores and prevent reinfection.<br>
            <br>
            Treatment:<br>
            - Apply fungicides specifically labeled for Stecklenberger disease, following the recommended application schedule.''','Seeding'
        ),
        (
            'Bacterial Canker',
            '''Symptoms:<br>
            - Dark, sunken lesions on branches and twigs, which may ooze a sticky substance.<br>
            - Gumming or oozing from infected areas, leading to dieback of shoots.<br>
            - Leaf wilting and yellowing, which can lead to significant tree stress.<br>
            <br>
            Causes:<br>
            - Bacterial infection (Pseudomonas syringae) often exacerbated by winter injury or mechanical damage to the tree.<br>
            <br>
            Preventive Measures:<br>
            - Prune infected branches and sterilize tools to prevent spreading the bacteria.<br>
            - Avoid wounding trees during cold weather or when they are wet.<br>
            - Apply protective bactericides in early spring before symptoms appear.<br>
            <br>
            Treatment:<br>
            - If infection is detected, prune out infected areas and apply appropriate bactericides as recommended.''','Seeding'
        ),
        (
            'Aphids',
            '''Symptoms:<br>
            - Curling and yellowing of leaves, which can stunt plant growth.<br>
            - Presence of sticky honeydew on leaves and fruit, attracting sooty mold.<br>
            - Ants may be seen tending to aphids, indicating their presence.<br>
            <br>
            Causes:<br>
            - Small sap-sucking insects that feed on plant sap, weakening the plant and potentially transmitting viruses.<br>
            <br>
            Preventive Measures:<br>
            - Introduce natural predators like ladybugs and lacew
                    - Introduce natural predators like ladybugs and lacewings to help control aphid populations.<br>
            - Regularly inspect plants for early signs of infestation to catch them before they spread.<br>
            <br>
            Treatment:<br>
            - Use insecticidal soap or neem oil to control populations, applying according to the product instructions.''','Seeding'
        )
        ]
        for name, description, stage in apple_diseases_seeding:
            disease = Disease(plant_id=apple.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for Apple at the vegetative stage
        apple_diseases_vegetative = [
            (
                'Powdery Mildew',
                '''Symptoms:<br>
                - Powdery mildew is a fungal disease that appears as white powdery spots on leaves and stems.<br>
                - It can cause stunted growth and reduced fruit yield.<br>
                <br>
                Control Methods:<br>
                - Use fungicides specifically labeled for powdery mildew control.<br>
                - Practice good garden hygiene by removing infected plant debris and ensuring good air circulation.''','Vegetative'
            ),
            (
                'Fruit Tree Canker',
                '''Symptoms:<br>
                - Fruit tree canker causes sunken, dead areas on the bark, often with a gummy exudate.<br>
                - It can girdle branches or trunks, leading to dieback.<br>
                <br>
                Control Methods:<br>
                - Prune out infected areas to prevent the spread of the disease.<br>
                - Apply protective fungicides to healthy tissue to prevent infection.''','Vegetative'
            ),
            (
                'Apple Scab',
                '''Symptoms:<br>
                - Apple scab causes dark, scabby lesions on leaves, fruit, and stems.<br>
                - It can lead to defoliation and reduced fruit quality.<br>
                <br>
                Control Methods:<br>
                - Manage by applying fungicides during the growing season.<br>
                - Remove and destroy infected plant debris to reduce the risk of reinfection.''','Vegetative'
            ),
            (
                'Silver Leaf',
                '''Symptoms:<br>
                - Silver leaf is a fungal disease that causes a silvery sheen on leaves due to air spaces forming within the leaf tissues.<br>
                - It can kill branches and entire trees.<br>
                <br>
                Control Methods:<br>
                - Treat by pruning affected areas to prevent further spread.<br>
                - Use appropriate fungicides as recommended for silver leaf disease.''','Vegetative'
            )
        ]
        for name, description, stage in apple_diseases_vegetative:
            disease = Disease(plant_id=apple.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for Apple at the flowering stage
        apple_diseases_flowering = [
            (
                'Root and Collar Rot',
                '''Symptoms:<br>
                - Root and collar rot causes the roots and lower trunk to rot, leading to wilting and yellowing of leaves.<br>
                - Infected plants may exhibit stunted growth and overall decline in vigor.<br>
                <br>
                Causes:<br>
                - This disease is often caused by soil-borne fungi, particularly in poorly drained soils.<br>
                <br>
                Control Methods:<br>
                - Improve soil drainage by amending the soil with organic matter and ensuring proper grading.<br>
                - Avoid overwatering and monitor soil moisture levels.<br>
                - Apply fungicides specifically labeled for root and collar rot, following the manufacturer's instructions.<br>
                - Remove and destroy infected plants to prevent the spread of the disease.''','Flowering'
            ),
            (
                'Powdery Mildew',
                '''Symptoms:<br>
                - Powdery mildew appears as white powdery spots on leaves and stems.<br>
                - Infected leaves may become distorted, leading to stunted growth and reduced fruit yield.<br>
                <br>
                Causes:<br>
                - This fungal disease thrives in warm, dry conditions and can spread rapidly in crowded plantings.<br>
                <br>
                Control Methods:<br>
                - Use fungicides specifically labeled for powdery mildew control, applying at the first sign of infection.<br>
                - Practice good garden hygiene by removing infected plant debris and ensuring good air circulation around plants.<br>
                - Consider planting resistant varieties if available.''','Flowering'
            ),
            (
                'Apple Scab',
                '''Symptoms:<br>
                - Apple scab causes dark, scabby lesions on leaves, fruit, and stems.<br>
                - Infected leaves may yellow and drop prematurely, leading to defoliation and reduced fruit quality.<br>
                <br>
                Causes:<br>
                - This disease is caused by the fungal pathogen Venturia inaequalis, which thrives in wet conditions.<br>
                <br>
                Control Methods:<br>
                - Manage by applying fungicides during the growing season, especially during wet weather.<br>
                - Remove and destroy infected plant debris to reduce the risk of reinfection.<br>
                - Practice crop rotation and avoid planting susceptible varieties in the same location year after year.''','Flowering'
            ),
            (
                'Brown Rot',
                '''Symptoms:<br>
                - Brown rot causes browning and rotting of fruit, often with white fungal growth (conidia) on the surface.<br>
                - Infected fruit may become mummified and remain attached to the tree.<br>
                <br>
                Causes:<br>
                - This disease is caused by the fungal pathogen Monilinia fructigena, which can infect blossoms, fruit, and twigs.<br>
                <br>
                Control Methods:<br>
                - Remove and destroy infected fruit and mummified remains to reduce the spread of the disease.<br>
                - Apply fungicides during the flowering stage and again at fruit set, following the manufacturer's recommendations.<br>
                - Ensure good air circulation around trees to reduce humidity levels that favor fungal growth.''','Flowering'
            ),
            (
                'Silver Leaf',
                '''Symptoms:<br>
                - Silver leaf is a fungal disease that causes a silvery sheen on leaves due to air spaces forming within the leaf tissues.<br>
                - It can lead to branch dieback and, in severe cases, kill entire trees.<br>
                <br>
                Causes:<br>
                - This disease is caused by the fungus Chondrostereum purpureum, which often enters through wounds or pruning cuts.<br>
                <br>
                Control Methods:<br>
                - Treat by pruning affected areas to prevent further spread of the disease.<br>
                - Use appropriate fungicides as recommended for silver leaf disease.<br>
                - Avoid wounding trees during wet conditions and ensure proper pruning techniques are followed.''','Flowering'
            ),
            (
                'Dead Arm',
                '''Symptoms:<br>
                - Dead arm causes dieback of branches, with cankers and dead areas on the wood.<br>
                - Infected branches may exhibit wilting leaves and reduced fruit production.<br>
                <br>
                Causes:<br>
                - This disease is often caused by fungal pathogens such as Botryosphaeria spp., which can enter through wounds or stressed areas of the tree.<br>
                <br>
                Control Methods:<br>
                - Control involves pruning out infected areas to prevent the spread of the disease.<br>
                        - Apply fungicides to healthy tissue as a preventive measure, especially during periods of high humidity.<br>
                - Ensure proper tree care practices, including adequate watering and fertilization, to reduce stress on the tree.<br>
                - Monitor for signs of infection and act quickly to prune out affected areas to maintain tree health.''','Flowering'
            )
        ]
        for name, description, stage in apple_diseases_flowering:
            disease = Disease(plant_id=apple.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for Apple at the fruiting stage
        apple_diseases_fruiting = [
            ('Root and Collar Rot', '''Symptoms:<br>Root and collar rot causes the roots and lower trunk to rot, leading to wilting and yellowing of leaves.<br>Control involves improving soil drainage and applying fungicides.''', 'Fruiting'),
            ('Powdery Mildew', '''Symptoms:<br>Powdery mildew is a fungal disease that appears as white powdery spots on leaves and stems. It can cause stunted growth and reduced fruit yield.<br>Control methods include using fungicides and practicing good garden hygiene.''', 'Fruiting'),
            ('Fruit Tree Canker', '''Symptoms:<br>Fruit tree canker causes sunken, dead areas on the bark, often with a gummy exudate. It can girdle branches or trunks, leading to dieback.<br>Prune out infected areas and apply protective fungicides.''', 'Fruiting'),
            ('Apple Scab', '''Symptoms:<br>Apple scab causes dark, scabby lesions on leaves, fruit, and stems. It can lead to defoliation and reduced fruit quality.<br>Manage by applying fungicides and removing infected plant debris.''', 'Fruiting'),
            ('Brown Rot', '''Symptoms:<br>Brown rot causes browning and rotting of fruit, often with white fungal growth.<br>Control involves removing infected fruit and applying fungicides.''', 'Fruiting'),
            ('Blossom Blight', '''Symptoms:<br>Blossom blight causes browning and wilting of flowers, and can lead to fruit rot.<br>Control involves removing infected flowers and applying fungicides.''', 'Fruiting')
        ]
        for name, description, stage in apple_diseases_fruiting:
            disease = Disease(plant_id=apple.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for apple at the harvesting stage
        apple_diseases_harvesting = [
            (
                'Apple Root and Collar Rot',
                '''Symptoms:<br>
                - Wilting of leaves, often starting from the lower leaves.<br>
                - Yellowing and dropping of leaves, leading to reduced canopy density.<br>
                - Dark, sunken lesions at the base of the trunk, which may ooze sap.<br>
                - Root decay and poor fruit development, resulting in smaller fruit size.<br>
                - Overall decline in tree vigor, making trees more susceptible to other diseases.<br><br>
                Causes:<br>
                - Fungal pathogens such as *Phytophthora* and *Armillaria* species thrive in wet, poorly drained soils.<br>
                - Overwatering and poor soil aeration can exacerbate the problem.<br>
                - Soil compaction can limit root growth and increase disease susceptibility.<br>
                - High humidity and temperature can promote fungal growth.<br>
                - Wounding of the tree during cultivation can provide entry points for pathogens.<br><br>
                Preventive Measures:<br>
                - Ensure proper drainage in orchards to prevent waterlogging.<br>
                - Avoid overwatering and monitor soil moisture levels regularly.<br>
                - Use resistant rootstock varieties when planting to enhance disease resistance.<br>
                - Implement crop rotation to reduce pathogen load in the soil.<br>
                - Regularly inspect trees for early signs of disease and take action promptly.<br><br>
                Treatment:<br>
                - Remove and destroy infected plants to prevent spread.<br>
                - Apply fungicides to the soil as a preventive measure, especially in high-risk areas.<br>
                - Improve soil drainage and aeration through tillage and organic amendments.<br>
                - Consider soil solarization to reduce pathogen populations.<br>
                - Monitor and manage irrigation practices to maintain optimal soil moisture.<br>
                ''',
                'Harvesting'
            ),
            (
                'Brown Rot',
                '''Symptoms:<br>
                - Brown, soft rot on fruit, often starting at the blossom end and spreading quickly.<br>
                - Fruit may shrivel and become mummified, hanging on the tree or falling to the ground.<br>
                - Fungal spores may appear as a grayish-brown powder on the surface, especially in humid conditions.<br>
                - Affected fruit may emit a foul odor as decay progresses.<br>
                - Premature fruit drop can occur, leading to significant yield loss.<br><br>
                Causes:<br>
                - Caused by the fungus *Monilinia fructigena*, which thrives in warm, humid conditions.<br>
                - Infection can occur through wounds or during wet weather, especially after rain.<br>
                - High nitrogen fertilization can lead to excessive vegetative growth, increasing susceptibility.<br>
                - Poor air circulation around fruit can create a favorable environment for the fungus.<br>
                - Infected fruit left on the tree or ground can serve as a source of inoculum.<br><br>
                Preventive Measures:<br>
                - Practice good sanitation by removing and destroying infected fruit and debris.<br>
                - Avoid overhead irrigation to reduce humidity around the fruit and minimize wetness.<br>
                - Thin fruit to improve air circulation and reduce humidity levels.<br>
                - Monitor weather conditions and apply fungicides proactively during high-risk periods.<br>
                - Implement integrated pest management (IPM) strategies to reduce overall disease pressure.<br><br>
                Treatment:<br>
                - Apply fungicides at the onset of flowering and again at fruit set to protect against infection.<br>
                - Remove and destroy mummified fruit and debris from the orchard to reduce inoculum.<br>
                - Consider using biological control agents that target the brown rot pathogen.<br>
                - Monitor for signs of infection and treat promptly to prevent spread.<br>
                - Ensure proper post-harvest handling to minimize damage and decay.<br><br>
                ''',
                'Harvesting'
            ),
            (
                'Silver Leaf',
                '''Symptoms:<br>
                - Leaves exhibit a silvery sheen and may curl or become distorted, often starting from the top.<br>
                - Branch dieback and overall decline in tree vigor, leading to reduced fruit yield.<br>
                - In severe cases, trees may die, with bark cracking and peeling.<br>
                - Affected trees may show stunted growth and poor fruit quality.<br>
                - Increased susceptibility to other pests and diseases due to weakened health.<br><br>
                Causes:<br>
                - Caused by the fungus *Chondrostereum purpureum*, which infects through wounds.<br>
                - Often associated with poor tree health and environmental stress, such as drought.<br>
                - Wounding during pruning or mechanical damage can facilitate
                        - Wounding during pruning or mechanical damage can facilitate infection.<br>
                - High humidity and poor air circulation can promote fungal growth.<br>
                - Soil nutrient deficiencies can weaken trees, making them more susceptible to infection.<br><br>
                Preventive Measures:<br>
                - Prune trees to remove dead or diseased wood and improve air circulation.<br>
                - Avoid wounding trees during pruning or harvesting to minimize entry points for pathogens.<br>
                - Maintain tree health through proper nutrition, watering, and pest management.<br>
                - Use resistant varieties when available to reduce the risk of infection.<br>
                - Regularly inspect trees for early signs of disease and take action promptly.<br><br>
                Treatment:<br>
                - Remove and destroy infected branches to prevent further spread of the disease.<br>
                - Apply fungicides to prevent further spread, especially after pruning.<br>
                - Improve overall tree health through proper fertilization and irrigation practices.<br>
                - Monitor for signs of secondary infections and treat as necessary.<br>
                - Consider using biological control agents that target the silver leaf pathogen.<br>
                ''',
                'Harvesting'
            ),
            (
                'Scooty Blotch of Apple',
                '''Symptoms:<br>
                - Dark, sooty spots on the surface of the fruit, which can be mistaken for bruising.<br>
                - Affected areas may become sunken and lead to fruit decay, especially in humid conditions.<br>
                - Reduced marketability due to cosmetic damage, leading to economic losses.<br>
                - In severe cases, the fruit may develop a foul odor as it decays.<br>
                - The presence of the fungus can also lead to secondary infections by other pathogens.<br><br>
                Causes:<br>
                - Caused by the fungus *Gloeodes pomigena*, which thrives in humid conditions.<br>
                - Often associated with poor air circulation and high humidity in the orchard.<br>
                - Overcrowding of trees can create a microclimate conducive to fungal growth.<br>
                - Wounds on the fruit from handling or environmental factors can facilitate infection.<br>
                - Infected fruit left on the tree or ground can serve as a source of inoculum.<br><br>
                Preventive Measures:<br>
                - Ensure proper spacing between trees for air circulation and sunlight penetration.<br>
                - Avoid excessive moisture on fruit surfaces by managing irrigation practices.<br>
                - Implement good orchard hygiene practices, including removing fallen fruit.<br>
                - Monitor weather conditions and apply fungicides proactively during high-risk periods.<br>
                - Use resistant varieties when available to reduce the risk of infection.<br><br>
                Treatment:<br>
                - Apply fungicides during the growing season, especially before harvest, to protect fruit.<br>
                - Remove and destroy affected fruit to prevent spread and reduce inoculum.<br>
                - Consider using biological control agents that target the scooty blotch pathogen.<br>
                - Monitor for signs of infection and treat promptly to prevent further spread.<br>
                - Ensure proper post-harvest handling to minimize damage and decay.<br><br>
                ''',
                'Harvesting'
            ),
            (
                'Fruit Cracking',
                '''Symptoms:<br>
                - Cracks or splits in the skin of the fruit, often around the stem or blossom end.<br>
                - Cracked fruit may be more susceptible to rot and pests, leading to further damage.<br>
                - Aesthetic damage reduces marketability, affecting sales and profits.<br>
                - Cracks may vary in size and depth, sometimes exposing the inner fruit.<br>
                - In severe cases, fruit may drop prematurely due to structural weakness.<br><br>
                Causes:<br>
                - Caused by rapid changes in moisture levels, often due to heavy rainfall or irrigation.<br>
                - Nutritional imbalances, particularly excess nitrogen, can contribute to rapid growth.<br>
                - High humidity and temperature fluctuations can exacerbate the problem.<br>
                - Poor soil structure can lead to uneven moisture retention.<br>
                - Inconsistent watering practices can stress the fruit and lead to cracking.<br><br>
                Preventive Measures:<br>
                - Maintain consistent soil moisture levels to avoid rapid fluctuations in water availability.<br>
                - Use mulch to retain soil moisture and reduce evaporation, especially during dry spells.<br>
                - Monitor and adjust fertilization practices to avoid excessive nitrogen application.<br>
                - Implement proper irrigation practices to ensure even moisture distribution.<br>
                - Regularly inspect fruit for early signs of cracking and take action promptly.<br><br>
                Treatment:<br>
                - There is no direct treatment for cracked fruit; focus on prevention.<br>
                - Harvest fruit promptly to minimize damage and reduce the risk of rot.<br>
                - Remove and destroy severely cracked fruit to prevent the spread of pathogens.<br>
                - Ensure proper post-harvest handling to minimize further damage and decay.<br>
                - Educate workers on handling practices to reduce mechanical injuries to fruit.<br><br>
                ''',
                'Harvesting'
            )
        ]
        for name, description, stage in apple_diseases_harvesting:
            disease = Disease(plant_id=apple.id, name=name, description=description, stage=stage)
            db.session.add(disease)
        
        # Add disease data for Grape at the seeding stage
        grape = Plant.query.filter_by(name='Grapes').first()
        grape_diseases_seeding = [
            (
                'Black Mould',
                '''Symptoms:<br>
                - Black mould causes black, sooty patches on leaves, stems, and fruit.<br>
                - Affected areas may appear fuzzy or velvety, especially in humid conditions.<br>
                - Leaves may yellow and drop prematurely due to severe infection.<br>
                - Fruit may become unmarketable due to cosmetic damage.<br>
                - In severe cases, the plant's overall health may decline.<br><br>
                
                Causes:<br>
                - Caused by fungal pathogens that thrive in warm, humid environments.<br>
                - Poor air circulation and high humidity levels can exacerbate the problem.<br>
                - Overcrowding of plants can create a microclimate conducive to fungal growth.<br>
                - Infected plant debris can serve as a source of inoculum.<br>
                - Excessive nitrogen fertilization can promote lush growth, increasing susceptibility.<br><br>
                
                Preventive Measures:<br>
                - Use resistant varieties when available to reduce the risk of infection.<br>
                - Improve air circulation around plants by proper spacing and pruning.<br>
                - Avoid overhead irrigation to minimize leaf wetness.<br>
                - Regularly remove and destroy infected plant debris.<br>
                - Monitor humidity levels and apply fungicides as needed.<br><br>
                
                Treatment:<br>
                - Apply fungicides at the first sign of infection to protect healthy tissue.<br>
                - Remove and destroy severely infected plant parts to reduce disease spread.<br>
                - Ensure proper sanitation practices in the vineyard.<br>
                - Consider using biological control agents that target the black mould pathogen.<br>
                - Monitor for signs of secondary infections and treat as necessary.<br><br>
                ''',
                'Seeding'
            ),
            (
                'Damping Off of Seedlings',
                '''Symptoms:<br>
                - Damping off causes young seedlings to rot at the base, leading to wilting and death.<br>
                - Affected seedlings may appear water-soaked and collapse suddenly.<br>
                - The soil surface may appear fuzzy or moldy due to fungal growth.<br>
                - Seedlings may fail to emerge or develop stunted growth.<br>
                - High humidity and poor drainage can exacerbate the problem.<br><br>
                
                Causes:<br>
                - Caused by various fungal pathogens, including *Pythium* and *Rhizoctonia* species.<br>
                - Overwatering and poor soil drainage create favorable conditions for pathogens.<br>
                - Using contaminated soil or planting materials can introduce pathogens.<br>
                - High humidity levels can promote fungal growth and seedling decline.<br>
                - Stress factors such as temperature fluctuations can weaken seedlings.<br><br>
                
                Preventive Measures:<br>
                - Use sterilized soil or seed-starting mix to reduce pathogen load.<br>
                - Ensure proper drainage in seedling trays or pots.<br>
                - Avoid overwatering and monitor soil moisture levels closely.<br>
                - Space seedlings adequately to improve air circulation.<br>
                - Implement crop rotation to reduce pathogen populations in the soil.<br><br>
                
                Treatment:<br>
                - Remove and destroy infected seedlings to prevent further spread.<br>
                - Apply fungicides to the soil as a preventive measure.<br>
                - Improve air circulation around seedlings to reduce humidity.<br>
                - Consider using biological control agents that target damping-off pathogens.<br>
                - Monitor for signs of infection and treat promptly to prevent losses.<br><br>
                ''',
                'Seeding'
            ),
            (
                'Aphids',
                '''Symptoms:<br>
                - Aphids are small, sap-sucking insects that cause curling and yellowing of leaves.<br>
                - Infested leaves may become distorted and stunted in growth.<br>
                - A sticky substance (honeydew) may be present on leaves and fruit.<br>
                - Ants may be attracted to honeydew, indicating aphid presence.<br>
                - Severe infestations can lead to reduced plant vigor and yield.<br><br>
                
                Causes:<br>
                - Aphids thrive in warm, dry conditions and can reproduce rapidly.<br>
                - They are often introduced to the garden through infested plants.<br>
                - Poor plant health can make plants more susceptible to aphid infestations.<br>
                - Weeds can serve as alternate hosts for aphids, increasing their populations.<br>
                - Environmental stress factors can lead to increased vulnerability.<br><br>
                
                Preventive Measures:<br>
                - Monitor plants regularly for early signs of aphid infestations.<br>
                - Encourage natural predators like ladybugs and lacewings in the garden.<br>
                - Use insecticidal soaps or neem oil to control aphid populations.<br>
                - Remove weeds and other potential hosts around the planting area.<br>
                - Maintain overall plant health through proper watering and fertilization.<br><br>
                
                Treatment:<br>
                - Apply insecticidal soaps or horticultural oils to affected plants.<br>
                - Introduce beneficial insects like ladybugs to help control aphid populations.<br>
                - Remove heavily infested leaves or shoots to reduce the population.<br>
                - Monitor for signs of secondary infections due to aphid feeding.<br>
                - Reapply treatments as necessary, following label instructions.<br><br>
                ''',
                'Seeding'
            ),
            (
                'Transparent Scale',
                '''Symptoms:<br>
                - Transparent scale insects cause yellowing and drop of leaves by sucking sap from the plants.<br>
                - Infested leaves may appear sticky due to honeydew excretion.<br>
                - Scale insects can be seen as small, waxy bumps on stems and leaves.<br>
                - Severe infestations can lead to stunted growth and reduced vigor.<br>
                - Affected plants may become more susceptible to other pests and diseases.<br><br>
                
                Causes:<br>
                - Transparent scale is caused by small, sap-sucking insects that thrive in warm conditions.<br>
                - They can be introduced through infested plants or by wind.<br>
                - Poor plant health can make plants more susceptible to scale infestations.<br>
                - High humidity and overcrowding can promote scale development.<br>
                - Environmental stress factors can lead to increased vulnerability.<br><br>
                
                Preventive Measures:<br>
                - Monitor plants regularly for early signs of scale infestations.<br>
                - Maintain good air circulation around plants to reduce humidity.<br>
                - Use resistant varieties when available to reduce the risk of infestation.<br>
                - Remove and destroy heavily infested plant parts to reduce spread.<br>
                - Encourage natural predators like ladybugs and parasitic wasps.<br><br>
                
                Treatment:<br>
                - Apply horticultural oils or insecticidal soaps to affected plants.<br>
                - Remove and destroy heavily infested leaves or stems.<br>
                - Monitor for signs of secondary infections due to scale feeding.<br>
                - Reapply treatments as necessary, following label instructions.<br>
                - Consider using systemic insecticides for severe infestations.<br><br>
                ''',
                'Seeding'
            ),
            (
                'Slugs and Snails',
                '''Symptoms:<br>
                - Slugs and snails cause irregular holes in leaves and fruits.<br>
                - Affected leaves may appear ragged and have a characteristic slime trail.<br>
                - They may also feed on young seedlings, leading to stunted growth.<br>
                - In severe cases, they can cause significant damage to the crop.<br>
                - Their feeding can lead to increased susceptibility to diseases.<br><br>
                
                Causes:<br>
                - Slugs and snails thrive in moist, humid conditions and are often found in gardens.<br>
                - They are attracted to decaying organic matter and damp environments.<br>
                - Overwatering and poor drainage can create favorable conditions for them.<br>
                - They can be introduced through contaminated soil or plant materials.<br>
                - Environmental stress factors can lead to increased vulnerability.<br><br>
                
                Preventive Measures:<br>
                - Use barriers such as copper tape or diatomaceous earth around plants.<br>
                - Remove debris and organic matter that can provide shelter for slugs and snails.<br>
                - Water plants in the morning to reduce moisture levels at night.<br>
                - Encourage natural predators like birds and toads in the garden.<br>
                - Monitor for signs of infestation and take action promptly.<br><br>
                
                Treatment:<br>
                - Use baits specifically designed for slugs and snails to reduce their populations.<br>
                - Handpick slugs and snails in the early morning or late evening.<br>
                - Apply organic methods such as beer traps to attract and drown them.<br>
                - Monitor for signs of secondary infections due to slug feeding.<br>
                - Reapply treatments as necessary, following label instructions.<br><br>
                ''',
                'Seeding'
            )
        ]        
        for name, description, stage in grape_diseases_seeding:
            disease = Disease(plant_id=grape.id, name=name, description=description, stage=stage)
            db.session.add(disease)
        
        # Add disease data for Grape at the vegetative stage
        grape_diseases_vegetative = [
            (
                'Fusarium Wilt',
                '''Symptoms:<br>
                - Yellowing of leaves, starting from the lower leaves and progressing upward.<br>
                - Wilting of leaves, even when soil moisture is adequate.<br>
                - Dark streaks or lesions may appear on the stems.<br>
                - Affected plants may exhibit stunted growth and reduced yield.<br>
                - In severe cases, the plant may die suddenly.<br><br>
                
                Causes:<br>
                - Caused by the fungus *Fusarium oxysporum*, which infects through the roots.<br>
                - Soil-borne pathogen that thrives in warm, moist conditions.<br>
                - Overwatering and poor drainage can exacerbate the problem.<br>
                - Wounding of roots during cultivation can facilitate infection.<br>
                - Susceptibility increases in stressed plants due to drought or nutrient deficiencies.<br><br>
                
                Preventive Measures:<br>
                - Use resistant grape varieties when available.<br>
                - Ensure proper soil drainage and avoid overwatering.<br>
                - Practice crop rotation to reduce pathogen load in the soil.<br>
                - Maintain healthy soil with organic amendments to improve plant vigor.<br>
                - Regularly inspect plants for early signs of disease and take action promptly.<br><br>
                
                Treatment:<br>
                - Remove and destroy infected plants to prevent spread.<br>
                - Apply fungicides as a preventive measure in high-risk areas.<br>
                - Improve soil drainage and aeration to reduce pathogen populations.<br>
                - Consider soil solarization to reduce soil-borne pathogens.<br>
                - Monitor and manage irrigation practices to maintain optimal soil moisture.<br>
                ''',
                'Vegetative'
            ),
            (
                'Phoma Blight',
                '''Symptoms:<br>
                - Dark, water-soaked lesions on leaves, stems, and fruit.<br>
                - Leaves may yellow and drop prematurely due to severe infection.<br>
                - Affected fruit may develop dark spots and rot.<br>
                - Infected stems may exhibit cankers, leading to dieback.<br>
                - Overall decline in plant vigor and yield reduction.<br><br>
                
                Causes:<br>
                - Caused by the fungus *Phoma viticola*, which thrives in wet conditions.<br>
                - High humidity and poor air circulation can exacerbate the problem.<br>
                - Overcrowding of plants can create a microclimate conducive to fungal growth.<br>
                - Infected plant debris can serve as a source of inoculum.<br>
                - Excessive nitrogen fertilization can promote lush growth, increasing susceptibility.<br><br>
                
                Preventive Measures:<br>
                - Use resistant varieties when available to reduce the risk of infection.<br>
                - Improve air circulation around plants by proper spacing and pruning.<br>
                - Avoid overhead irrigation to minimize leaf wetness.<br>
                - Regularly remove and destroy infected plant debris.<br>
                - Monitor humidity levels and apply fungicides as needed.<br><br>
                
                Treatment:<br>
                - Apply fungicides at the first sign of infection to protect healthy tissue.<br>
                - Remove and destroy severely infected plant parts to reduce disease spread.<br>
                - Ensure proper sanitation practices in the vineyard.<br>
                - Consider using biological control agents that target the Phoma blight pathogen.<br>
                - Monitor for signs of secondary infections and treat as necessary.<br>
                ''',
                'Vegetative'
            ),
            (
                'Anthracnose of Grape',
                '''Symptoms:<br>
                - Dark, sunken lesions on leaves, stems, and fruit.<br>
                - Leaves may exhibit irregular shapes and yellowing around the edges.<br>
                - Infected fruit may develop dark, water-soaked spots that lead to rot.<br>
                - Affected stems may show dieback and cankers.<br>
                - Overall decline in plant health and reduced yield.<br><br>
                
                Causes:<br>
                - Caused by the fungus *Colletotrichum* species, which thrives in warm, humid conditions.<br>
                - Infection can occur through wounds or during wet weather.<br>
                - High humidity and poor air circulation can promote fungal growth.<br>
                - Infected plant debris can serve as a source of inoculum.<br>
                - Excessive nitrogen fertilization can lead to lush growth, increasing susceptibility.<br><br>
                
                        Preventive Measures:<br>
                - Use resistant varieties when available to reduce the risk of infection.<br>
                - Improve air circulation around plants by proper spacing and pruning.<br>
                - Avoid overhead irrigation to minimize leaf wetness.<br>
                - Regularly remove and destroy infected plant debris.<br>
                - Monitor humidity levels and apply fungicides as needed.<br><br>
                
                Treatment:<br>
                - Apply fungicides at the first sign of infection to protect healthy tissue.<br>
                - Remove and destroy severely infected plant parts to reduce disease spread.<br>
                - Ensure proper sanitation practices in the vineyard.<br>
                - Consider using biological control agents that target the anthracnose pathogen.<br>
                - Monitor for signs of secondary infections and treat as necessary.<br>
                ''',
                'Vegetative'
            ),
            (
                'Dead Arm',
                '''Symptoms:<br>
                - Symptoms include wilting and yellowing of leaves, often starting from the top.<br>
                - Dark streaks may appear on the stems, leading to dieback.<br>
                - Affected vines may show stunted growth and reduced fruit yield.<br>
                - Infected areas may develop cankers, leading to further decline.<br>
                - Overall decline in plant health and vigor.<br><br>
                
                Causes:<br>
                - Caused by the fungus *Eutypa lata*, which infects through pruning wounds.<br>
                - High humidity and poor air circulation can exacerbate the problem.<br>
                - Overcrowding of plants can create a microclimate conducive to fungal growth.<br>
                - Infected plant debris can serve as a source of inoculum.<br>
                - Environmental stress factors can lead to increased vulnerability.<br><br>
                
                Preventive Measures:<br>
                - Use resistant varieties when available to reduce the risk of infection.<br>
                - Ensure proper pruning techniques to minimize wounds.<br>
                - Improve air circulation around plants by proper spacing and pruning.<br>
                - Regularly remove and destroy infected plant debris.<br>
                - Monitor humidity levels and apply fungicides as needed.<br><br>
                
                Treatment:<br>
                - Remove and destroy infected plant parts to reduce disease spread.<br>
                - Apply fungicides as a preventive measure in high-risk areas.<br>
                - Improve soil drainage and aeration to reduce pathogen populations.<br>
                - Consider soil solarization to reduce soil-borne pathogens.<br>
                - Monitor and manage irrigation practices to maintain optimal soil moisture.<br>
                ''',
                'Vegetative'
            ),
            (
                'Botryosphaeria Dieback',
                '''Symptoms:<br>
                - Symptoms include wilting and yellowing of leaves, often starting from the top.<br>
                - Dark streaks may appear on the stems, leading to dieback.<br>
                - Affected vines may show stunted growth and reduced fruit yield.<br>
                - Infected areas may develop cankers, leading to further decline.<br>
                - Overall decline in plant health and vigor.<br><br>
                
                Causes:<br>
                - Caused by the fungus *Botryosphaeria* species, which infects through wounds.<br>
                - High humidity and poor air circulation can exacerbate the problem.<br>
                - Overcrowding of plants can create a microclimate conducive to fungal growth.<br>
                - Infected plant debris can serve as a source of inoculum.<br>
                - Environmental stress factors can lead to increased vulnerability.<br><br>
                
                Preventive Measures:<br>
                - Use resistant varieties when available to reduce the risk of infection.<br>
                - Ensure proper pruning techniques to minimize wounds.<br>
                - Improve air circulation around plants by proper spacing and pruning.<br>
                - Regularly remove and destroy infected plant debris.<br>
                - Monitor humidity levels and apply fungicides as needed.<br><br>
                
                Treatment:<br>
                - Remove and destroy infected plant parts to reduce disease spread.<br>
                - Apply fungicides as a preventive measure in high-risk areas.<br>
                - Improve soil drainage and aeration to reduce pathogen populations.<br>
                - Consider soil solarization to reduce soil-borne pathogens.<br>
                - Monitor and manage irrigation practices to maintain optimal soil moisture.<br>
                ''',
                'Vegetative'
            ),
            (
                'Powdery Mildew of Grape',
                '''Symptoms:<br>
                - White, powdery spots appear on leaves, stems, and fruit.<br>
                - Leaves may curl and distort, leading to reduced photosynthesis.<br>
                        - Infected fruit may develop a powdery coating, affecting quality.<br>
                - Severe infections can lead to premature leaf drop and reduced yield.<br><br>
                
                Causes:<br>
                - Caused by the fungus *Erysiphe necator*, which thrives in warm, dry conditions.<br>
                - High humidity and poor air circulation can exacerbate the problem.<br>
                - Overcrowding of plants can create a microclimate conducive to fungal growth.<br>
                - Infected plant debris can serve as a source of inoculum.<br>
                - Environmental stress factors can lead to increased vulnerability.<br><br>
                
                Preventive Measures:<br>
                - Use resistant varieties when available to reduce the risk of infection.<br>
                - Improve air circulation around plants by proper spacing and pruning.<br>
                - Avoid overhead irrigation to minimize leaf wetness.<br>
                - Regularly remove and destroy infected plant debris.<br>
                - Monitor humidity levels and apply fungicides as needed.<br><br>
                
                Treatment:<br>
                - Apply fungicides at the first sign of infection to protect healthy tissue.<br>
                - Remove and destroy severely infected plant parts to reduce disease spread.<br>
                - Ensure proper sanitation practices in the vineyard.<br>
                - Consider using biological control agents that target the powdery mildew pathogen.<br>
                - Monitor for signs of secondary infections and treat as necessary.<br>
                ''',
                'Vegetative'
            ),
            (
                'Grape Rust',
                '''Symptoms:<br>
                - Yellow to orange spots appear on the upper surface of leaves.<br>
                - The undersides of leaves may show orange, powdery pustules.<br>
                - Infected leaves may curl, yellow, and drop prematurely.<br>
                - Affected plants may exhibit stunted growth and reduced vigor.<br>
                - Severe infections can lead to significant yield loss.<br><br>
                
                Causes:<br>
                - Caused by the fungus *Puccinia* species, which requires moisture for spore germination.<br>
                - High humidity and wet conditions can exacerbate the problem.<br>
                - Overcrowding of plants can create a microclimate conducive to fungal growth.<br>
                - Infected plant debris can serve as a source of inoculum.<br>
                - Environmental stress factors can lead to increased vulnerability.<br><br>
                
                Preventive Measures:<br>
                - Use resistant varieties when available to reduce the risk of infection.<br>
                - Improve air circulation around plants by proper spacing and pruning.<br>
                - Avoid overhead irrigation to minimize leaf wetness.<br>
                - Regularly remove and destroy infected plant debris.<br>
                - Monitor humidity levels and apply fungicides as needed.<br><br>
                
                Treatment:<br>
                - Apply fungicides at the first sign of infection to protect healthy tissue.<br>
                - Remove and destroy severely infected plant parts to reduce disease spread.<br>
                - Ensure proper sanitation practices in the vineyard.<br>
                - Consider using biological control agents that target the grape rust pathogen.<br>
                - Monitor for signs of secondary infections and treat as necessary.<br>
                ''',
                'Vegetative'
            )
        ]
        for name, description, stage in grape_diseases_vegetative:
            disease = Disease(plant_id=grape.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for Grapes at the flowering stage
        grape_diseases_flowering = [
            (
                'Verticillium Wilt',
                '''Symptoms:<br>
                - Yellowing of leaves, starting from the lower leaves and progressing upward.<br>
                - Wilting of leaves, even when soil moisture is adequate.<br>
                - Dark streaks or lesions may appear on the stems.<br>
                - Affected plants may exhibit stunted growth and reduced yield.<br>
                - In severe cases, the plant may die suddenly.<br><br>
                
                Causes:<br>
                - Caused by the fungus *Verticillium dahliae*, which infects through the roots.<br>
                - Soil-borne pathogen that thrives in warm, moist conditions.<br>
                - Overwatering and poor drainage can exacerbate the problem.<br>
                - Wounding of roots during cultivation can facilitate infection.<br>
                - Susceptibility increases in stressed plants due to drought or nutrient deficiencies.<br><br>
                
                Preventive Measures:<br>
                - Use resistant grape varieties when available.<br>
                - Ensure proper soil drainage and avoid overwatering.<br>
                - Practice crop rotation to reduce pathogen load in the soil.<br>
                - Maintain healthy soil with organic amendments to improve plant vigor.<br>
                - Regularly inspect plants for early signs of disease and take action promptly.<br><br>
                
                Treatment:<br>
                - Remove and destroy infected plants to prevent spread.<br>
                - Apply fungicides as a preventive measure in high-risk areas.<br>
                - Improve soil drainage and aeration to reduce pathogen populations.<br>
                - Consider soil solarization to reduce soil-borne pathogens.<br>
                - Monitor and manage irrigation practices to maintain optimal soil moisture.<br>
                ''',
                'Flowering'
            ),
            (
                'Fusarium Wilt',
                '''Symptoms:<br>
                - Yellowing of leaves, starting from the lower leaves and progressing upward.<br>
                - Wilting of leaves, even when soil moisture is adequate.<br>
                - Dark streaks or lesions may appear on the stems.<br>
                - Affected plants may exhibit stunted growth and reduced yield.<br>
                - In severe cases, the plant may die suddenly.<br><br>
                
                Causes:<br>
                - Caused by the fungus *Fusarium oxysporum*, which infects through the roots.<br>
                - Soil-borne pathogen that thrives in warm, moist conditions.<br>
                - Overwatering and poor drainage can exacerbate the problem.<br>
                - Wounding of roots during cultivation can facilitate infection.<br>
                - Susceptibility increases in stressed plants due to drought or nutrient deficiencies.<br><br>
                
                Preventive Measures:<br>
                - Use resistant grape varieties when available.<br>
                - Ensure proper soil drainage and avoid overwatering.<br>
                - Practice crop rotation to reduce pathogen load in the soil.<br>
                - Maintain healthy soil with organic amendments to improve plant vigor.<br>
                - Regularly inspect plants for early signs of disease and take action promptly.<br><br>
                
                Treatment:<br>
                - Remove and destroy infected plants to prevent spread.<br>
                - Apply fungicides as a preventive measure in high-risk areas.<br>
                - Improve soil drainage and aeration to reduce pathogen populations.<br>
                - Consider soil solarization to reduce soil-borne pathogens.<br>
                - Monitor and manage irrigation practices to maintain optimal soil moisture.<br>
                ''',
                'Flowering'
            ),
            (
                'Anthracnose of Grape',
                '''Symptoms:<br>
                - Dark, sunken lesions on leaves, stems, and fruit.<br>
                - Leaves may exhibit irregular shapes and yellowing around the edges.<br>
                - Infected fruit may develop dark, water-soaked spots that lead to rot.<br>
                - Affected stems may show dieback and cankers.<br>
                - Overall decline in plant health and reduced yield.<br><br>
                
                Causes:<br>
                - Caused by the fungus *Colletotrichum* species, which thrives in warm, humid conditions.<br>
                - Infection can occur through wounds or during wet weather.<br>
                - High humidity and poor air circulation can promote fungal growth.<br>
                - Infected plant debris can serve as a source of inoculum.<br>
                - Excessive nitrogen fertilization can lead to lush growth, increasing susceptibility.<br><br>
                
                        Preventive Measures:<br>
                - Use resistant varieties when available to reduce the risk of infection.<br>
                - Improve air circulation around plants by proper spacing and pruning.<br>
                - Avoid overhead irrigation to minimize leaf wetness.<br>
                - Regularly remove and destroy infected plant debris.<br>
                - Monitor humidity levels and apply fungicides as needed.<br><br>
                
                Treatment:<br>
                - Apply fungicides at the first sign of infection to protect healthy tissue.<br>
                - Remove and destroy severely infected plant parts to reduce disease spread.<br>
                - Ensure proper sanitation practices in the vineyard.<br>
                - Consider using biological control agents that target the anthracnose pathogen.<br>
                - Monitor for signs of secondary infections and treat as necessary.<br>
                ''',
                'Flowering'
            ),
            (
                'Dead Arm',
                '''Symptoms:<br>
                - Symptoms include wilting and yellowing of leaves, often starting from the top.<br>
                - Dark streaks may appear on the stems, leading to dieback.<br>
                - Affected vines may show stunted growth and reduced fruit yield.<br>
                - Infected areas may develop cankers, leading to further decline.<br>
                - Overall decline in plant health and vigor.<br><br>
                
                Causes:<br>
                - Caused by the fungus *Eutypa lata*, which infects through pruning wounds.<br>
                - High humidity and poor air circulation can exacerbate the problem.<br>
                - Overcrowding of plants can create a microclimate conducive to fungal growth.<br>
                - Infected plant debris can serve as a source of inoculum.<br>
                - Environmental stress factors can lead to increased vulnerability.<br><br>
                
                Preventive Measures:<br>
                - Use resistant varieties when available to reduce the risk of infection.<br>
                - Ensure proper pruning techniques to minimize wounds.<br>
                - Improve air circulation around plants by proper spacing and pruning.<br>
                - Regularly remove and destroy infected plant debris.<br>
                - Monitor humidity levels and apply fungicides as needed.<br><br>
                
                Treatment:<br>
                - Remove and destroy infected plant parts to reduce disease spread.<br>
                - Apply fungicides as a preventive measure in high-risk areas.<br>
                - Improve soil drainage and aeration to reduce pathogen populations.<br>
                - Consider soil solarization to reduce soil-borne pathogens.<br>
                - Monitor and manage irrigation practices to maintain optimal soil moisture.<br>
                ''',
                'Flowering'
            ),
            (
                'Black Rot of Grape',
                '''Symptoms:<br>
                - Black, round spots appear on leaves, stems, and fruit.<br>
                - Infected fruit may shrivel and become mummified.<br>
                - Leaves may yellow and drop prematurely due to severe infection.<br>
                - Affected stems may show dark lesions and dieback.<br>
                - Overall decline in plant health and reduced yield.<br><br>
                
                Causes:<br>
                - Caused by the fungus *Guignardia bidwellii*, which thrives in warm, humid conditions.<br>
                - Infection can occur through wounds or during wet weather.<br>
                - High humidity and poor air circulation can promote fungal growth.<br>
                - Infected plant debris can serve as a source of inoculum.<br>
                - Excessive nitrogen fertilization can lead to lush growth, increasing susceptibility.<br><br>
                
                Preventive Measures:<br>
                - Use resistant varieties when available to reduce the risk of infection.<br>
                - Improve air circulation around plants by proper spacing and pruning.<br>
                - Avoid overhead irrigation to minimize leaf wetness.<br>
                - Regularly remove and destroy infected plant debris.<br>
                - Monitor humidity levels and apply fungicides as needed.<br><br>
                
                Treatment:<br>
                - Apply fungicides at the first sign of infection to protect healthy tissue.<br>
                - Remove and destroy severely infected plant parts to reduce disease spread.<br>
                - Ensure proper sanitation practices in the vineyard.<br>
                - Consider using biological control agents that target the black rot pathogen.<br>
                - Monitor for signs of secondary infections and treat as necessary.<br>
                ''',
                'Flowering'
            ),
            (
                'Foot Rot',
                '''Symptoms:<br>
                - Symptoms include wilting and yellowing of leaves, often starting from the base.<br>
                - Dark, water-soaked lesions may appear at the base of the plant.<br>
                        - Affected plants may exhibit stunted growth and reduced yield.<br>
                - In severe cases, the plant may die due to root rot.<br><br>
                
                Causes:<br>
                - Caused by various soil-borne pathogens, including *Phytophthora* species.<br>
                - High moisture levels and poor drainage can exacerbate the problem.<br>
                - Overwatering and compacted soil can create favorable conditions for pathogens.<br>
                - Wounding of roots during cultivation can facilitate infection.<br>
                - Susceptibility increases in stressed plants due to drought or nutrient deficiencies.<br><br>
                
                Preventive Measures:<br>
                - Ensure proper soil drainage and avoid overwatering.<br>
                - Use resistant grape varieties when available.<br>
                - Practice crop rotation to reduce pathogen load in the soil.<br>
                - Maintain healthy soil with organic amendments to improve plant vigor.<br>
                - Regularly inspect plants for early signs of disease and take action promptly.<br><br>
                
                Treatment:<br>
                - Remove and destroy infected plants to prevent spread.<br>
                - Apply fungicides as a preventive measure in high-risk areas.<br>
                - Improve soil drainage and aeration to reduce pathogen populations.<br>
                - Consider soil solarization to reduce soil-borne pathogens.<br>
                - Monitor and manage irrigation practices to maintain optimal soil moisture.<br>
                ''',
                'Flowering'
            ),
            (
                'Downy Mildew of Grape',
                '''Symptoms:<br>
                - Yellowish-green spots appear on the upper surface of leaves.<br>
                - A white, downy growth may be visible on the undersides of leaves.<br>
                - Infected leaves may curl and drop prematurely.<br>
                - Affected fruit may develop brown lesions and rot.<br>
                - Overall decline in plant health and reduced yield.<br><br>
                
                Causes:<br>
                - Caused by the fungus *Plasmopara viticola*, which thrives in warm, humid conditions.<br>
                - Infection can occur during wet weather, especially in spring.<br>
                - High humidity and poor air circulation can promote fungal growth.<br>
                - Infected plant debris can serve as a source of inoculum.<br>
                - Excessive nitrogen fertilization can lead to lush growth, increasing susceptibility.<br><br>
                
                Preventive Measures:<br>
                - Use resistant varieties when available to reduce the risk of infection.<br>
                - Improve air circulation around plants by proper spacing and pruning.<br>
                - Avoid overhead irrigation to minimize leaf wetness.<br>
                - Regularly remove and destroy infected plant debris.<br>
                - Monitor humidity levels and apply fungicides as needed.<br><br>
                
                Treatment:<br>
                - Apply fungicides at the first sign of infection to protect healthy tissue.<br>
                - Remove and destroy severely infected plant parts to reduce disease spread.<br>
                - Ensure proper sanitation practices in the vineyard.<br>
                - Consider using biological control agents that target the downy mildew pathogen.<br>
                - Monitor for signs of secondary infections and treat as necessary.<br>
                ''',
                'Flowering'
            ),
            (
                'Thrips',
                '''Symptoms:<br>
                - Small, slender insects that cause stippling and discoloration on leaves.<br>
                - Leaves may curl or become distorted due to feeding damage.<br>
                - Affected flowers may drop prematurely or fail to develop properly.<br>
                - Infested fruit may show scarring and reduced quality.<br>
                - Severe infestations can lead to reduced plant vigor and yield.<br><br>
                
                Causes:<br>
                - Thrips are small, sap-sucking insects that thrive in warm, dry conditions.<br>
                - They can be introduced to the garden through infested plants or by wind.<br>
                - Poor plant health can make plants more susceptible to thrips infestations.<br>
                - Weeds can serve as alternate hosts for thrips, increasing their populations.<br>
                - Environmental stress factors can lead to increased vulnerability.<br><br>
                
                Preventive Measures:<br>
                - Monitor plants regularly for early signs of thrips infestations.<br>
                - Encourage natural predators like ladybugs and lacewings in the garden.<br>
                - Use insecticidal soaps or neem oil to control thrips populations.<br>
                - Remove weeds and other potential hosts around the planting area.<br>
                - Maintain overall plant health through proper watering and fertilization.<br><br>
                
                        Treatment:<br>
                - Apply insecticidal soaps or horticultural oils to affected plants.<br>
                - Introduce beneficial insects like ladybugs to help control thrips populations.<br>
                - Remove heavily infested leaves or shoots to reduce the population.<br>
                - Monitor for signs of secondary infections due to thrips feeding.<br>
                - Reapply treatments as necessary, following label instructions.<br>
                ''',
                'Flowering'
            )
        ]
        for name, description, stage in grape_diseases_flowering:
            disease = Disease(plant_id=grape.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for Grape at the fruiting stage
        grape_diseases_fruiting = [
            (
                'Verticillium Wilt',
                '''Symptoms:<br>
                - Yellowing of leaves, starting from the lower leaves and progressing upward.<br>
                - Wilting of leaves, even when soil moisture is adequate.<br>
                - Dark streaks or lesions may appear on the stems.<br>
                - Affected plants may exhibit stunted growth and reduced yield.<br>
                - In severe cases, the plant may die suddenly.<br><br>
                
                Causes:<br>
                - Caused by the fungus *Verticillium dahliae*, which infects through the roots.<br>
                - Soil-borne pathogen that thrives in warm, moist conditions.<br>
                - Overwatering and poor drainage can exacerbate the problem.<br>
                - Wounding of roots during cultivation can facilitate infection.<br>
                - Susceptibility increases in stressed plants due to drought or nutrient deficiencies.<br><br>
                
                Preventive Measures:<br>
                - Use resistant grape varieties when available.<br>
                - Ensure proper soil drainage and avoid overwatering.<br>
                - Practice crop rotation to reduce pathogen load in the soil.<br>
                - Maintain healthy soil with organic amendments to improve plant vigor.<br>
                - Regularly inspect plants for early signs of disease and take action promptly.<br><br>
                
                Treatment:<br>
                - Remove and destroy infected plants to prevent spread.<br>
                - Apply fungicides as a preventive measure in high-risk areas.<br>
                - Improve soil drainage and aeration to reduce pathogen populations.<br>
                - Consider soil solarization to reduce soil-borne pathogens.<br>
                - Monitor and manage irrigation practices to maintain optimal soil moisture.<br>
                ''',
                'Fruiting'
            ),
            (
                'Fusarium Wilt',
                '''Symptoms:<br>
                - Yellowing of leaves, starting from the lower leaves and progressing upward.<br>
                - Wilting of leaves, even when soil moisture is adequate.<br>
                - Dark streaks or lesions may appear on the stems.<br>
                - Affected plants may exhibit stunted growth and reduced yield.<br>
                - In severe cases, the plant may die suddenly.<br><br>
                
                Causes:<br>
                - Caused by the fungus *Fusarium oxysporum*, which infects through the roots.<br>
                - Soil-borne pathogen that thrives in warm, moist conditions.<br>
                - Overwatering and poor drainage can exacerbate the problem.<br>
                - Wounding of roots during cultivation can facilitate infection.<br>
                - Susceptibility increases in stressed plants due to drought or nutrient deficiencies.<br><br>
                
                Preventive Measures:<br>
                - Use resistant grape varieties when available.<br>
                - Ensure proper soil drainage and avoid overwatering.<br>
                - Practice crop rotation to reduce pathogen load in the soil.<br>
                - Maintain healthy soil with organic amendments to improve plant vigor.<br>
                - Regularly inspect plants for early signs of disease and take action promptly.<br><br>
                
                Treatment:<br>
                - Remove and destroy infected plants to prevent spread.<br>
                - Apply fungicides as a preventive measure in high-risk areas.<br>
                - Improve soil drainage and aeration to reduce pathogen populations.<br>
                - Consider soil solarization to reduce soil-borne pathogens.<br>
                - Monitor and manage irrigation practices to maintain optimal soil moisture.<br>
                ''',
                'Fruiting'
            ),
            (
                'Botrytis Blight',
                '''Symptoms:<br>
                - Gray, fuzzy mold appears on fruit clusters, especially in humid conditions.<br>
                - Infected fruit may become soft and mushy, leading to rot.<br>
                - Leaves may show water-soaked spots and premature yellowing.<br>
                - Affected clusters may shrivel and become unmarketable.<br>
                - Overall decline in plant health and reduced yield.<br><br>
                
                Causes:<br>
                - Caused by the fungus *Botrytis cinerea*, which thrives in wet, humid conditions.<br>
                - High humidity and poor air circulation can exacerbate the problem.<br>
                - Overcrowding of plants can create a microclimate conducive to fungal growth.<br>
                - Infected plant debris can serve as a source of inoculum.<br>
                - Excessive nitrogen fertilization can lead to lush growth, increasing susceptibility.<br><br>
                
                Preventive Measures:<br>
                - Use resistant varieties when available to reduce the risk of infection.<br>
                - Improve air circulation around plants by proper spacing and pruning.<br>
                - Avoid overhead irrigation to minimize leaf wetness.<br>
                - Regularly remove and destroy infected plant debris.<br>
                - Monitor humidity levels and apply fungicides as needed.<br><br>
                
                Treatment:<br>
                - Apply fungicides at the first sign of infection to protect healthy tissue.<br>
                - Remove and destroy severely infected plant parts to reduce disease spread.<br>
                - Ensure proper sanitation practices in the vineyard.<br>
                - Consider using biological control agents that target the Botrytis pathogen.<br>
                - Monitor for signs of secondary infections and treat as necessary.<br>
                ''',
                'Fruiting'
            ),
            (
                'Anthracnose of Grape',
                '''Symptoms:<br>
                - Dark, sunken lesions on leaves, stems, and fruit.<br>
                - Leaves may exhibit irregular shapes and yellowing around the edges.<br>
                - Infected fruit may develop dark, water-soaked spots that lead to rot.<br>
                - Affected stems may show dieback and cankers.<br>
                - Overall decline in plant health and reduced yield.<br><br>
                
                Causes:<br>
                - Caused by the fungus *Colletotrichum* species, which thrives in warm, humid conditions.<br>
                - Infection can occur through wounds or during wet weather.<br>
                - High humidity and poor air circulation can promote fungal growth.<br>
                - Infected plant debris can serve as a source of inoculum.<br>
                - Excessive nitrogen fertilization can lead to lush growth, increasing susceptibility.<br><br>
                
                Preventive Measures:<br>
                - Use resistant varieties when available to reduce the risk of infection.<br>
                - Improve air circulation around plants by proper spacing and pruning.<br>
                - Avoid overhead irrigation to minimize leaf wetness.<br>
                - Regularly remove and destroy infected plant debris.<br>
                - Monitor humidity levels and apply fungicides as needed.<br><br>
                
                Treatment:<br>
                - Apply fungicides at the first sign of infection to protect healthy tissue.<br>
                - Remove and destroy severely infected plant parts to reduce disease spread.<br>
                - Ensure proper sanitation practices in the vineyard.<br>
                - Consider using biological control agents that target the anthracnose pathogen.<br>
                - Monitor for signs of secondary infections and treat as necessary.<br>
                ''',
                'Fruiting'
            ),
            (
                'Bitter Rot of Grape',
                '''Symptoms:<br>
                        - Dark, sunken lesions appear on fruit, often starting at the stem end.<br>
                - Infected fruit may become soft and mushy, leading to rot.<br>
                - Affected fruit may shrivel and develop a foul odor.<br>
                - Leaves may show yellowing and premature drop due to severe infection.<br>
                - Overall decline in plant health and reduced yield.<br><br>
                
                Causes:<br>
                - Caused by the fungus *Glomerella cingulata*, which thrives in warm, humid conditions.<br>
                - Infection can occur through wounds or during wet weather.<br>
                - High humidity and poor air circulation can promote fungal growth.<br>
                - Infected plant debris can serve as a source of inoculum.<br>
                - Excessive nitrogen fertilization can lead to lush growth, increasing susceptibility.<br><br>
                
                Preventive Measures:<br>
                - Use resistant varieties when available to reduce the risk of infection.<br>
                - Improve air circulation around plants by proper spacing and pruning.<br>
                - Avoid overhead irrigation to minimize leaf wetness.<br>
                - Regularly remove and destroy infected plant debris.<br>
                - Monitor humidity levels and apply fungicides as needed.<br><br>
                
                Treatment:<br>
                - Apply fungicides at the first sign of infection to protect healthy tissue.<br>
                - Remove and destroy severely infected plant parts to reduce disease spread.<br>
                - Ensure proper sanitation practices in the vineyard.<br>
                - Consider using biological control agents that target the bitter rot pathogen.<br>
                - Monitor for signs of secondary infections and treat as necessary.<br>
                ''',
                'Fruiting'
            ),
            (
                'Spider Mites',
                '''Symptoms:<br>
                - Tiny, spider-like pests that cause stippling and discoloration on leaves.<br>
                - Leaves may appear speckled, yellow, or bronze due to feeding damage.<br>
                - Fine webbing may be visible on the undersides of leaves.<br>
                - Affected leaves may curl and drop prematurely.<br>
                - Severe infestations can lead to reduced plant vigor and yield.<br><br>
                
                Causes:<br>
                - Spider mites thrive in hot, dry conditions and can reproduce rapidly.<br>
                - They are often introduced to the garden through infested plants.<br>
                - Poor plant health can make plants more susceptible to spider mite infestations.<br>
                - Dusty conditions can exacerbate mite problems by reducing natural predation.<br><br>
                
                Preventive Measures:<br>
                - Monitor plants regularly for early signs of spider mite infestations.<br>
                - Encourage natural predators like ladybugs and predatory mites in the garden.<br>
                - Use insecticidal soaps or neem oil to control spider mite populations.<br>
                - Keep plants well-watered to reduce stress and improve vigor.<br>
                - Maintain good air circulation around plants to reduce humidity.<br><br>
                
                Treatment:<br>
                - Apply insecticidal soaps or horticultural oils to affected plants.<br>
                - Introduce beneficial insects like ladybugs to help control spider mite populations.<br>
                - Remove heavily infested leaves or shoots to reduce the population.<br>
                - Monitor for signs of secondary infections due to spider mite feeding.<br>
                - Reapply treatments as necessary, following label instructions.<br>
                ''',
                'Fruiting'
            ),
            (
                'Mealybug',
                '''Symptoms:<br>
                - White, cottony masses appear on leaves, stems, and fruit.<br>
                - Leaves may yellow and drop prematurely due to sap-sucking damage.<br>
                - A sticky substance (honeydew) may be present on leaves and fruit.<br>
                - Ants may be attracted to honeydew, indicating mealybug presence.<br>
                - Severe infestations can lead to reduced plant vigor and yield.<br><br>
                
                Causes:<br>
                - Mealybugs are small, sap-sucking insects that thrive in warm, dry conditions.<br>
                - They can be introduced to the garden through infested plants.<br>
                - Poor plant health can make plants more susceptible to mealybug infestations.<br>
                - Weeds can serve as alternate hosts for mealybugs, increasing their populations.<br><br>
                
                Preventive Measures:<br>
                - Monitor plants regularly for early signs of mealybug infestations.<br>
                - Encourage natural predators like ladybugs and lacewings in the garden.<br>
                - Use insecticidal soaps or neem oil to control mealybug populations.<br>
                - Remove weeds and other potential hosts around the planting area.<br>
                - Maintain overall plant health through proper watering and fertilization.<br><br>
                
                Treatment:<br>
                - Apply insecticidal soaps or horticultural oils to affected plants.<br>
                - Remove and destroy heavily infested leaves or stems.<br>
                - Monitor for signs of secondary infections due to mealybug feeding.<br>
                - Reapply treatments as necessary, following label instructions.<br>
                ''',
                'Fruiting'
            )
        ]
        for name, description, stage in grape_diseases_fruiting:
            disease = Disease(plant_id=grape.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for Grape at the harvesting stage
        grape_diseases_harvesting = [
            (
                'Black Vine Thrips',
                '''Symptoms:<br>
                - Tiny, slender insects that cause stippling and discoloration on leaves and fruit.<br>
                - Leaves may appear speckled, yellow, or bronze due to feeding damage.<br>
                - Affected fruit may show scarring and reduced quality.<br>
                - Severe infestations can lead to reduced plant vigor and yield.<br>
                - Fine webbing may be visible on the undersides of leaves.<br><br>
                
                Causes:<br>
                - Black vine thrips thrive in warm, dry conditions and can reproduce rapidly.<br>
                - They are often introduced to the garden through infested plants.<br>
                - Poor plant health can make plants more susceptible to thrips infestations.<br>
                - Dusty conditions can exacerbate thrips problems by reducing natural predation.<br><br>
                
                Preventive Measures:<br>
                - Monitor plants regularly for early signs of thrips infestations.<br>
                - Encourage natural predators like ladybugs and lacewings in the garden.<br>
                - Use insecticidal soaps or neem oil to control thrips populations.<br>
                - Keep plants well-watered to reduce stress and improve vigor.<br>
                - Maintain good air circulation around plants to reduce humidity.<br><br>
                
                Treatment:<br>
                - Apply insecticidal soaps or horticultural oils to affected plants.<br>
                - Introduce beneficial insects like ladybugs to help control thrips populations.<br>
                - Remove heavily infested leaves or shoots to reduce the population.<br>
                - Monitor for signs of secondary infections due to thrips feeding.<br>
                - Reapply treatments as necessary, following label instructions.<br>
                ''',
                'Harvesting'
            ),
            (
                'Spittlebugs',
                '''Symptoms:<br>
                - Spittlebugs create frothy masses on leaves and stems, resembling spit.<br>
                - Affected leaves may show yellowing and wilting due to sap-sucking damage.<br>
                - Infested plants may exhibit stunted growth and reduced vigor.<br>
                - Severe infestations can lead to reduced fruit yield and quality.<br>
                - The presence of spittle masses can hinder photosynthesis.<br><br>
                
                Causes:<br>
                - Spittlebugs are small, sap-sucking insects that thrive in warm, humid conditions.<br>
                - They can be introduced to the garden through infested plants.<br>
                - Poor plant health can make plants more susceptible to spittlebug infestations.<br>
                - Weeds can serve as alternate hosts for spittlebugs, increasing their populations.<br><br>
                
                Preventive Measures:<br>
                - Monitor plants regularly for early signs of spittlebug infestations.<br>
                - Encourage natural predators like birds and beneficial insects in the garden.<br>
                - Use insecticidal soaps or neem oil to control spittlebug populations.<br>
                - Remove weeds and other potential hosts around the planting area.<br>
                - Maintain overall plant health through proper watering and fertilization.<br><br>
                
                Treatment:<br>
                - Apply insecticidal soaps or horticultural oils to affected plants.<br>
                - Remove and destroy heavily infested leaves or stems.<br>
                - Monitor for signs of secondary infections due to spittlebug feeding.<br>
                - Reapply treatments as necessary, following label instructions.<br>
                ''',
                'Harvesting'
            ),
            (
                'Potassium Deficiency',
                '''Symptoms:<br>
                - Leaves may show yellowing between the veins, leading to a mottled appearance.<br>
                - Margins of older leaves may become scorched or brown.<br>
                - Affected plants may exhibit stunted growth and reduced fruit quality.<br>
                - Overall decline in plant health and vigor.<br>
                - In severe cases, fruit may be small and poorly developed.<br><br>
                
                Causes:<br>
                - Potassium deficiency can occur due to poor soil fertility or imbalanced fertilization.<br>
                - High rainfall or excessive irrigation can leach potassium from the soil.<br>
                - Soil pH levels that are too high or too low can affect potassium availability.<br>
                - Compacted soil can restrict root access to nutrients.<br><br>
                
                Preventive Measures:<br>
                - Conduct soil tests to determine nutrient levels and adjust fertilization accordingly.<br>
                - Apply potassium-rich fertilizers as needed to maintain proper nutrient balance.<br>
                - Ensure proper soil drainage and aeration to promote healthy root growth.<br>
                - Monitor irrigation practices to avoid leaching of nutrients.<br>
                - Maintain healthy soil with organic amendments to improve nutrient retention.<br><br>
                
                Treatment:<br>
                - Apply potassium fertilizers to correct deficiencies based on soil test results.<br>
                - Foliar applications of potassium can provide a quick boost to affected plants.<br>
                - Monitor and adjust fertilization practices to maintain optimal nutrient levels.<br>
                - Ensure proper watering practices to support nutrient uptake.<br>
                - Regularly inspect plants for signs of nutrient deficiencies and take action promptly.<br>
                ''',
                'Harvesting'
            ),
            (
                'Slugs and Snails',
                '''Symptoms:<br>
                - Slugs and snails cause irregular holes in leaves and fruits.<br>
                - Affected leaves may appear ragged and have a characteristic slime trail.<br>
                - They may also feed on young fruit, leading to scarring and decay.<br>
                - In severe cases, they can cause significant damage to the crop.<br>
                - Their feeding can lead to increased susceptibility to diseases.<br><br>
                
                Causes:<br>
                - Slugs and snails thrive in moist, humid conditions and are often found in gardens.<br>
                - They are attracted to decaying organic matter and damp environments.<br>
                - Overwatering and poor drainage can create favorable conditions for them.<br>
                - They can be introduced through contaminated soil or plant materials.<br><br>
                
                Preventive Measures:<br>
                - Use barriers such as copper tape or diatomaceous earth around plants.<br>
                - Remove debris and organic matter that can provide shelter for slugs and snails.<br>
                - Water plants in the morning to reduce moisture levels at night.<br>
                - Encourage natural predators like birds and toads in the garden.<br>
                - Monitor for signs of infestation and take action promptly.<br><br>
                
                Treatment:<br>
                - Use baits specifically designed for slugs and snails to reduce their populations.<br>
                - Handpick slugs and snails in the early morning or late evening.<br>
                - Apply organic methods such as beer traps to attract and drown them.<br>
                - Monitor for signs of secondary infections due to slug feeding.<br>
                - Reapply treatments as necessary, following label instructions.<br>
                ''',
                'Harvesting'
            ),
            (
                'Angular Leaf Scorch',
                '''Symptoms:<br>
                - Leaves may show angular, yellowish patches between the veins.<br>
                - Affected leaves may curl and become brittle.<br>
                - In severe cases, leaves may drop prematurely.<br>
                - Overall decline in plant health and reduced yield.<br>
                - Symptoms may be more pronounced during hot, dry weather.<br><br>
                
                Causes:<br>
                - Caused by environmental stress factors, including drought and high temperatures.<br>
                - Nutrient deficiencies, particularly potassium, can exacerbate symptoms.<br>
                - Poor soil drainage and compacted soil can restrict root access to water.<br>
                - High salinity levels in the soil can lead to leaf scorch.<br><br>
                
                Preventive Measures:<br>
                - Ensure proper irrigation practices to maintain consistent soil moisture.<br>
                        - Conduct soil tests to determine nutrient levels and adjust fertilization accordingly.<br>
                - Improve soil drainage and aeration to promote healthy root growth.<br>
                - Provide shade or windbreaks during extreme weather conditions.<br>
                - Monitor for signs of nutrient deficiencies and take action promptly.<br><br>
                
                Treatment:<br>
                - Apply potassium fertilizers to correct deficiencies based on soil test results.<br>
                - Ensure proper watering practices to support plant health.<br>
                - Remove affected leaves to reduce stress on the plant.<br>
                - Monitor and adjust fertilization practices to maintain optimal nutrient levels.<br>
                - Regularly inspect plants for signs of stress and take action as needed.<br>
                ''',
                'Harvesting'
            ),
            (
                'Sunburn',
                '''Symptoms:<br>
                - Leaves and fruit may show sunburned areas that appear bleached or scorched.<br>
                - Affected areas may become dry and papery, leading to tissue damage.<br>
                - Fruit may develop sunscald, resulting in poor quality and reduced marketability.<br>
                - Overall decline in plant health and reduced yield.<br>
                - Symptoms are more pronounced on exposed fruit and leaves.<br><br>
                
                Causes:<br>
                - Sunburn occurs due to excessive exposure to direct sunlight, especially during hot weather.<br>
                - Lack of adequate foliage cover can increase the risk of sunburn.<br>
                - Environmental stress factors, such as drought, can exacerbate the problem.<br>
                - High temperatures and low humidity can lead to increased evaporation and stress.<br><br>
                
                Preventive Measures:<br>
                - Ensure proper canopy management to provide adequate leaf cover for fruit.<br>
                - Use shade cloth or other protective measures during extreme heat.<br>
                - Maintain consistent watering practices to reduce plant stress.<br>
                - Monitor for signs of nutrient deficiencies that may weaken plant health.<br>
                - Regularly inspect plants for signs of stress and take action as needed.<br><br>
                
                Treatment:<br>
                - Remove severely sunburned leaves and fruit to reduce stress on the plant.<br>
                - Apply mulch around the base of the plants to retain soil moisture.<br>
                - Ensure proper irrigation practices to support plant health.<br>
                - Consider using reflective materials to reduce direct sunlight exposure.<br>
                - Monitor and adjust cultural practices to minimize stress during hot weather.<br>
                ''',
                'Harvesting'
            )
        ]
        for name, description, stage in grape_diseases_harvesting:
            disease = Disease(plant_id=grape.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        
        
        
        
        
        
        
        
        
        
        
        # Add disease data for Mango at the seeding stage
        mango = Plant.query.filter_by(name='Mango').first()
        mango_diseases_seeding =[
            ('Damping-Off of Seeding', '''Symptoms:<br>''', 'Seeding'),
            ('Bacterial Black Spot of Mango', '''Symptoms:<br>''', 'Seeding'),
            ('Aphids', '''Symptoms:<br>''', 'Seeding'),
            ('Black Citrus Aphid', '''Symptoms:<br>''', 'Seeding'),
            ('Termites', '''Symptoms:<br>''', 'Seeding'),
        ]
        for name, description, stage in mango_diseases_seeding:
            disease = Disease(plant_id=mango.id, name=name, description=description, stage=stage)
            db.session.add(disease)
        
        # Add disease data for Mango at the vegetative stage
        mango_diseases_vegetative = [
            ('Phoma Blight', '''Symptoms:<br>''', 'Vegetative'),
            ('Sooty Mold', '''Symptoms:<br>''', 'Vegetative'),
            ('Anthracnose', '''Symptoms:<br>''', 'Vegetative'),
            ('Mango Malformation', '''Symptoms:<br>''', 'Vegetative'),
            ('Mango Scab', '''Symptoms:<br>''', 'Vegetative'),
            ('Black Banded Disease', '''Symptoms:<br>''', 'Vegetative'),
            ('Mealybug', '''Symptoms:<br>''', 'Vegetative'),
        ]
        for name, description, stage in mango_diseases_vegetative:
            disease = Disease(plant_id=mango.id, name=name, description=description, stage=stage)
            db.session.add(disease)
        
        # Add disease data for Mango at the flowering stage
        mango_diseases_flowering = [
            ('Powdery Mildew of Mango', '''Symptoms:<br>''', 'Flowering'),
            ('Sooty Mold', '''Symptoms:<br>''', 'Flowering'),
            ('Mango Leaf Coating', '''Symptoms:<br>''', 'Flowering'),
            ('Whiteflies', '''Symptoms:<br>''', 'Flowering'),
            ('Leaf Miner Files', '''Symptoms:<br>''', 'Flowering'),
            ('Broad nosed Weevils', '''Symptoms:<br>''', 'Flowering'),
        ]
        for name, description, stage in mango_diseases_flowering:
            disease = Disease(plant_id=mango.id, name=name, description=description, stage=stage)
            db.session.add(disease)
        
        # Add disease data for Mango at the fruiting stage
        mango_diseases_fruiting = [
            ('Botrytis Blight', '''Symptoms:<br>''', 'Fruiting'),
            ('Black Shank', '''Symptoms:<br>''', 'Fruiting'),
            ('Fruit Molds', '''Symptoms:<br>''', 'Fruiting'),
            ('Mango Scab', '''Symptoms:<br>''', 'Fruiting'),
            ('Stem End Rot of Mango', '''Symptoms:<br>''', 'Fruiting'),
            ('Mango Fruit Fly', '''Symptoms:<br>''', 'Fruiting'),
            ('Cottony Cushion Scale', '''Symptoms:<br>''', 'Fruiting'),
            ('Mango Seed Borer ', '''Symptoms:<br>''', 'Fruiting'),
        ]
        for name, description, stage in mango_diseases_fruiting:
            disease = Disease(plant_id=mango.id, name=name, description=description, stage=stage)
            db.session.add(disease)
        
        # Add disease data for Mango at the harvesting stage
        mango_diseases_harvesting =[
            ('Mango Dieback Didease ', '''Symptoms:<br>''', 'Harvesting'),
            ('Botrytis Blight', '''Symptoms:<br>''', 'Harvesting'),
            ('Gummosis', '''Symptoms:<br>''', 'Harvesting'),
            ('Mediterranean Fruit Fly', '''Symptoms:<br>''', 'Harvesting'),
            ('Oleander Scale', '''Symptoms:<br>''', 'Harvesting'),
            ('Tussock Moths', '''Symptoms:<br>''', 'Harvesting'),
            ('Potassium Deficiency', '''Symptoms:<br>''', 'Harvesting'),
        ]
        for name, description, stage in mango_diseases_harvesting:
            disease = Disease(plant_id=mango.id, name=name, description=description, stage=stage)
            db.session.add(disease)


        # Add disease data for Onion at the seeding stage
        onion = Plant.query.filter_by(name='Onion').first()
        onion_diseases_seeding =[
            ('Downy Mildew', '''Symptoms:<br>''', 'Seeding'),
            ('White Rot', '''Symptoms:<br>''', 'Seeding'),
            ('Leek Rust', '''Symptoms:<br>''', 'Seeding'),
            ('White Grubs', '''Symptoms:<br>''', 'Seeding'),
            ('Onion Maggots', '''Symptoms:<br>''', 'Seeding'),
            ('Wireworms', '''Symptoms:<br>''', 'Seeding'),
        ] 
        for name, description, stage in onion_diseases_seeding:
            disease = Disease(plant_id=onion.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for onion at the vegetative stage
        onion_diseases_vegetative =[
            ('Calcium Deficiency', '''Symptoms:<br>''', 'Vegetative'),
            ('Magnesium Deficiency', '''Symptoms:<br>''', 'Vegetative'),
            ('Phosphorus Deficiency', '''Symptoms:<br>''', 'Vegetative'),
            ('Nematodes', '''Symptoms:<br>''', 'Vegetative'),
            ('Pesticide Damage', '''Symptoms:<br>''', 'Vegetative'),
        ]
        for name, description, stage in onion_diseases_vegetative:
            disease = Disease(plant_id=onion.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for onion at the flowering stage
        onion_diseases_flowering =[
            ('Powdery Mildew', '''Symptoms:<br>''', 'Flowering'),
            ('Foot and Collar Rot', '''Symptoms:<br>''', 'Flowering'),
            ('Stemphylium Leaf Blight of Onion', '''Symptoms:<br>''', 'Flowering'),
            ('Gray Leaf Spot', '''Symptoms:<br>''', 'Flowering'),
            ('Aster Yellows Phytoplasma', '''Symptoms:<br>''', 'Flowering'),
        ]
        for name, description, stage in onion_diseases_flowering:
            disease = Disease(plant_id=onion.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for onion at the fruiting stage
        onion_diseases_fruiting =[
            ('Powdery Mildew', '''Symptoms:<br>''', 'Fruiting'),
            ('Fusarium Wilt', '''Symptoms:<br>''', 'Fruiting'),
            ('Black Shank', '''Symptoms:<br>''', 'Fruiting'),
            ('Purple Blotch of Onion', '''Symptoms:<br>''', 'Fruiting'),
            ('Spider Miltes', '''Symptoms:<br>''', 'Fruiting'),
            ('Onion Yellow Dwarf', '''Symptoms:<br>''', 'Fruiting'),
        ]
        for name, description, stage in onion_diseases_fruiting:
            disease = Disease(plant_id=onion.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for onion at the harvesting stage
        onion_diseases_harvesting =[
            ('Steam Rot', '''Symptoms:<br>''', 'Harvesting'),
            ('Beet Armyworm', '''Symptoms:<br>''', 'Harvesting'),
            ('Helicoverpa Caterpillar', '''Symptoms:<br>''', 'Harvesting'),
            ('Sunburn', '''Symptoms:<br>''', 'Harvesting'),
        ]
        for name, description, stage in onion_diseases_harvesting:
            disease = Disease(plant_id=onion.id, name=name, description=description, stage=stage)
            db.session.add(disease)


        # Add disease data for Potato at the seeding stage
        potato = Plant.query.filter_by(name='Potato').first()
        potato_diseases_seeding =[
            ('Bottom Rot', '''Symptoms:<br>''', 'Seeding'),
            ('Damping-Off of Seeding ', '''Symptoms:<br>''', 'Seeding'),
            ('Potato X Virus', '''Symptoms:<br>''', 'Seeding'),
            ('Potato Mop Top Virus', '''Symptoms:<br>''', 'Seeding'),
            ('Slugs and Snails', '''Symptoms:<br>''', 'Seeding'),
        ]
        for name, description, stage in potato_diseases_seeding:
            disease = Disease(plant_id=potato.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for potato at the vegetative stage
        potato_diseases_vegetative =[
            ('Powdery Mildew', '''Symptoms:<br>''', 'Vegetative'),
            ('Bottom Rot', '''Symptoms:<br>''', 'Vegetative'),
            ('Atem Rot', '''Symptoms:<br>''', 'Vegetative'),
            ('Septoria Leaf Spot', '''Symptoms:<br>''', 'Vegetative'),
            ('Potato Leafroll Virus', '''Symptoms:<br>''', 'Vegetative'),
            ('Potato Y Virus', '''Symptoms:<br>''', 'Vegetative'),
            ('Potato S Virus', '''Symptoms:<br>''', 'Vegetative'),
            ('Hadda Beetle', '''Symptoms:<br>''', 'Vegetative'),
        ]
        for name, description, stage in potato_diseases_vegetative:
            disease = Disease(plant_id=potato.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for potato at the flowering stage
        potato_diseases_flowering =[
            ('Powdery Mildew', '''Symptoms:<br>''', 'Flowering'),
            ('Verticillium Wilt', '''Symptoms:<br>''', 'Flowering'),
            ('Alternaria Brown Spot', '''Symptoms:<br>''', 'Flowering'),
            ('Gray Leaf Spot', '''Symptoms:<br>''', 'Flowering'),
            ('Wet Rot', '''Symptoms:<br>''', 'Flowering'),
            ('Spider Miltes', '''Symptoms:<br>''', 'Flowering'),
        ]
        for name, description, stage in potato_diseases_flowering:
            disease = Disease(plant_id=potato.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for potato at the fruiting stage
        potato_diseases_fruiting =[
            ('Potato Late Blight', '''Symptoms:<br>''', 'Fruiting'),
            ('Bottom Rot', '''Symptoms:<br>''', 'Fruiting'),
            ('Southern Green Stink Bug', '''Symptoms:<br>''', 'Fruiting'),
            ('Tussock Moths', '''Symptoms:<br>''', 'Fruiting'),
            ('Scarab beetles', '''Symptoms:<br>''', 'Fruiting'),
            ('Cockchafer', '''Symptoms:<br>''', 'Fruiting'),
            ('Tobaccoo Caterpillar', '''Symptoms:<br>''', 'Fruiting'),
        ]
        for name, description, stage in potato_diseases_fruiting:
            disease = Disease(plant_id=potato.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for potato at the harvesting stage
        potato_diseases_harvesting =[
            ('Powdery Scab', '''Symptoms:<br>''', 'Harvesting'),
            ('Black Scurf', '''Symptoms:<br>''', 'Harvesting'),
            ('Sliver Scurf', '''Symptoms:<br>''', 'Harvesting'),
            ('Blackleg of Potato', '''Symptoms:<br>''', 'Harvesting'),
            ('Potato Scabs', '''Symptoms:<br>''', 'Harvesting'),
            ('Potato Tuber Moth', '''Symptoms:<br>''', 'Harvesting'),
            ('Frost Damage', '''Symptoms:<br>''', 'Harvesting'),
            ('Tuber Discoloration', '''Symptoms:<br>''', 'Harvesting'),
        ]
        for name, description, stage in potato_diseases_harvesting:
            disease = Disease(plant_id=potato.id, name=name, description=description, stage=stage)
            db.session.add(disease)


        # Add disease data for rose at the seeding stage
        rose = Plant.query.filter_by(name='Rose').first()
        rose_diseases_seeding =[
            ('Aphids', '''Symptoms:<br>''', 'Seeding'),
            ('Stecklenberger Disease', '''Symptoms:<br>''', 'Seeding'),
            ('Healthy', '''Symptoms:<br>''', 'Seeding'),
        ]
        for name, description, stage in rose_diseases_seeding:
            disease = Disease(plant_id=rose.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for rose at the vegetative stage
        rose_diseases_vegetative =[
           ('Black Spot', '''Symptoms:<br>''', 'Vegetative'), 
           ('Rose Mildew', '''Symptoms:<br>''', 'Vegetative'), 
           ('Spider Mites', '''Symptoms:<br>''', 'Vegetative'), 
           ('Leafcutter Bess', '''Symptoms:<br>''', 'Vegetative'), 
           ('Nitrogen Deficiency', '''Symptoms:<br>''', 'Vegetative'), 
           ('Boron Deficiency', '''Symptoms:<br>''', 'Vegetative'), 
        ]
        for name, description, stage in rose_diseases_vegetative:
            disease = Disease(plant_id=rose.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for rose at the flowering stage
        rose_diseases_flowering =[
            ('Whiteflies', '''Symptoms:<br>''', 'Flowering'), 
            ('Cottony Cushion Scale', '''Symptoms:<br>''', 'Flowering'),
            ('Rose Chafer', '''Symptoms:<br>''', 'Flowering'),
            ('Sulfer Deficiency', '''Symptoms:<br>''', 'Flowering'),
            ('Frost Damage', '''Symptoms:<br>''', 'Flowering'),
        ]
        for name, description, stage in rose_diseases_flowering:
            disease = Disease(plant_id=rose.id, name=name, description=description, stage=stage)
            db.session.add(disease)


        # Add disease data for rose at the fruiting stage
        rose_diseases_fruiting =[
            ('Rose Mildew ', '''Symptoms:<br>''', 'Fruiting'),
            ('Spider Mites', '''Symptoms:<br>''', 'Fruiting'),
            ('Rose Chafer', '''Symptoms:<br>''', 'Fruiting'),
            ('Magnesium Deficiency', '''Symptoms:<br>''', 'Fruiting'),
            ('Slugs and Snails', '''Symptoms:<br>''', 'Fruiting'),
            ('Sunburn', '''Symptoms:<br>''', 'Fruiting'),
        ]
        for name, description, stage in rose_diseases_fruiting:
            disease = Disease(plant_id=rose.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for rose at the harvesting stage
        rose_diseases_harvesting =[
            ('Potassium Deficiency ', '''Symptoms:<br>''', 'Harvesting'),
            ('Frost Damage', '''Symptoms:<br>''', 'Harvesting'),
            ('Sunburn', '''Symptoms:<br>''', 'Harvesting'),
        ]
        for name, description, stage in rose_diseases_harvesting:
            disease = Disease(plant_id=rose.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for sugarcane at the seeding stage
        sugarcane = Plant.query.filter_by(name='Sugarcane').first()
        sugarcane_diseases_seeding =[
            ('Red Rot', '''Symptoms:<br>''', 'Seeding'),
            ('Sugarcane Common Rust', '''Symptoms:<br>''', 'Seeding'),
            ('Wilt Disease of Sugarcane', '''Symptoms:<br>''', 'Seeding'),
            ('Eyespot of Sugarcane', '''Symptoms:<br>''', 'Seeding'),
            ('Early Shoot Borer', '''Symptoms:<br>''', 'Seeding'),
        ]
        for name, description, stage in sugarcane_diseases_seeding:
            disease = Disease(plant_id=sugarcane.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for sugarcane at the vegetative stage
        sugarcane_diseases_vegetative =[
            ('Powdery Mildew', '''Symptoms:<br>''', 'Vegetative'),
            ('Red Rot', '''Symptoms:<br>''', 'Vegetative'),
            ('Smut of Sugarcane', '''Symptoms:<br>''', 'Vegetative'),
            ('Foot and Collar Rot', '''Symptoms:<br>''', 'Vegetative'),
            ('Eyespot of Sugarcane', '''Symptoms:<br>''', 'Vegetative'),
            ('Bakanae and Foot Rot', '''Symptoms:<br>''', 'Vegetative'),
            ('Orange Rust Sugarcane', '''Symptoms:<br>''', 'Vegetative'),
            ('Leaf Scald of Sugarcane', '''Symptoms:<br>''', 'Vegetative'),
            ('Sugarcane Yellow Leaf Virus', '''Symptoms:<br>''', 'Vegetative'),
        ]
        for name, description, stage in sugarcane_diseases_vegetative:
            disease = Disease(plant_id=sugarcane.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for sugarcane at the flowering stage
        sugarcane_diseases_flowering =[
            ('Powdery Mildew', '''Symptoms:<br>''', 'Flowering'),
            ('Wilt Desease of Sugarcane', '''Symptoms:<br>''', 'Flowering'),
            ('Scooty Mold', '''Symptoms:<br>''', 'Flowering'),
            ('Pokkah Boeng', '''Symptoms:<br>''', 'Flowering'),
            ('Striga', '''Symptoms:<br>''', 'Flowering'),
            ('Mealybug', '''Symptoms:<br>''', 'Flowering'),
        ]
        for name, description, stage in sugarcane_diseases_flowering:
            disease = Disease(plant_id=sugarcane.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for sugarcane at the fruiting stage
        sugarcane_diseases_fruiting =[
            ('Ring Spot of Sugarcane', '''Symptoms:<br>''', 'Fruiting'),
            ('Pokkah Boeng', '''Symptoms:<br>''', 'Fruiting'),
            ('Bacterial Leaf Streak of Maize', '''Symptoms:<br>''', 'Fruiting'),
            ('Violet Stem Borer', '''Symptoms:<br>''', 'Fruiting'),
            ('Spiny Bollworm', '''Symptoms:<br>''', 'Fruiting'),
        ]
        for name, description, stage in sugarcane_diseases_fruiting:
            disease = Disease(plant_id=sugarcane.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for sugarcane at the harvesting stage
        sugarcane_diseases_harvesting =[
            ('Red Rot', '''Symptoms:<br>''', 'Harvesting'), 
            ('Fall Armyworm', '''Symptoms:<br>''', 'Harvesting'),   
            ('Spiny Bollworm', '''Symptoms:<br>''', 'Harvesting'), 
            ('Termites', '''Symptoms:<br>''', 'Harvesting'), 
            ('Tussock Moths', '''Symptoms:<br>''', 'Harvesting'), 
            ('Sunburn', '''Symptoms:<br>''', 'Harvesting'), 
        ]
        for name, description, stage in sugarcane_diseases_harvesting:
            disease = Disease(plant_id=sugarcane.id, name=name, description=description, stage=stage)
            db.session.add(disease)


        # Add disease data for Tomato at the seeding stage
        tomato = Plant.query.filter_by(name='Tomato').first()
        tomato_diseases_seeding = [
            ('Bottom Rot', '''Symptoms:<br>''', 'Seeding'), 
            ('Edema', '''Symptoms:<br>''', 'Seeding'), 
            ('Herbicide Growth Damage', '''Symptoms:<br>''', 'Seeding'), 
            ('Damping-Off of Seedings', '''Symptoms:<br>''', 'Seeding'), 
        ]
        for name, description, stage in tomato_diseases_seeding:
            disease = Disease(plant_id=tomato.id, name=name, description=description, stage=stage)
            db.session.add(disease)
        
        # Add disease data for Tomato at the vegetative stage
        tomato_diseases_vegetative = [
            ('Early Blight', '''Symptoms:<br> - Dark, concentric rings on leaves, stems, and fruits.<br> - Yellowing and withering of leaves.<br> - Brown or black lesions with a concentric ring pattern.<br>''', 'Vegetative'),
            ('Late Blight', 'A fungal disease causing water-soaked spots on leaves and fruit.', 'Vegetative'),
            ('Bacterial Wilt', 'A bacterial disease causing wilting and yellowing of leaves.', 'Vegetative'),
            ('Tomato Mosaic Virus', 'A viral disease causing mottling and yellowing of leaves.', 'Vegetative')
        ]
        for name, description, stage in tomato_diseases_vegetative:
            disease = Disease(plant_id=tomato.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for Tomato at the flowering stage
        tomato_diseases_flowering = [
            ('Verticillium Wilt', '''Symptoms:<br>''', 'Flowering'),
            ('Fusarium Wilt ', '''Symptoms:<br>''', 'Flowering'), 
            ('Leaf Mold of Tomato', '''Symptoms:<br>''', 'Flowering'),
            ('Tomato Spotted Wilt Virus', '''Symptoms:<br>''', 'Flowering'),
            ('Tomato Yellow Leaf Curl Virus', '''Symptoms:<br>''', 'Flowering'),
            ('Blossom Drop', '''Symptoms:<br>''', 'Flowering'),
        ]
        for name, description, stage in tomato_diseases_flowering:
            disease = Disease(plant_id=tomato.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for Tomato at the fruiting stage
        tomato_diseases_fruiting = [
            ('Fusarium Wilt', '''Symptoms:<br>''', 'Fruiting'),
            ('Stem Rot of Tomato', '''Symptoms:<br>''', 'Fruiting'),
            ('Tomato Late Blight', '''Symptoms:<br>''', 'Fruiting'),
            ('Leaf Mold of Tomato', '''Symptoms:<br>''', 'Fruiting'),
            ('Tobacco Streak Virus', '''Symptoms:<br>''', 'Fruiting'),
            ('Bacterial Canker of Tomato', '''Symptoms:<br>''', 'Fruiting'),
        ]
        for name, description, stage in tomato_diseases_fruiting:
            disease = Disease(plant_id=tomato.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for Tomato at the harvesting stage
        tomato_diseases_harvesting = [
            ('Tomato Late Blight', '''Symptoms:<br>''', 'Harvesting'),
            ('Stem Rot of Tomato', '''Symptoms:<br>''', 'Harvesting'),
            ('Tomato Spotted Wilt Virus ', '''Symptoms:<br>''', 'Harvesting'),
            ('Bright Line Brown Eye', '''Symptoms:<br>''', 'Harvesting'),
            ('Bacterial Spot and Speck of Tomato', '''Symptoms:<br>''', 'Harvesting'),
        ]
        for name, description, stage in tomato_diseases_harvesting:
            disease = Disease(plant_id=tomato.id, name=name, description=description, stage=stage)
            db.session.add(disease)


        # Add disease data for wheat at the seeding stage
        wheat = Plant.query.filter_by(name='Wheat').first()
        wheat_diseases_seeding = [
            ('Yellow Stripe Rust', '''Symptoms:<br>''', 'Seeding'),
            ('Septoria Tritici Boltch', '''Symptoms:<br>''', 'Seeding'),
            ('Leaf and Glume Boltch of Wheat', '''Symptoms:<br>''', 'Seeding'),
            ('Snow Mold of Cereals', '''Symptoms:<br>''', 'Seeding'),
        ]
        for name, description, stage in wheat_diseases_seeding:
            disease = Disease(plant_id=wheat.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for wheat at the vegetative stage
        wheat_diseases_vegetative = [
            ('Wheat aastem Rust', '''Symptoms:<br>''', 'Vegetative'),
            ('Septoria Tritici Blotch', '''Symptoms:<br>''', 'Vegetative'),
            ('Oriental Armyworm ', '''Symptoms:<br>''', 'Vegetative'),
            ('Violet Stem Borer', '''Symptoms:<br>''', 'Vegetative'),
            ('Rice Leafroller', '''Symptoms:<br>''', 'Vegetative'),
            ('Physiological Leaf Spot', '''Symptoms:<br>''', 'Vegetative'),
        ]
        for name, description, stage in wheat_diseases_vegetative:
            disease = Disease(plant_id=wheat.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for wheat at the flowering stage
        wheat_diseases_flowering = [
            ('Net Blotch ', '''Symptoms:<br>''', 'Flowering'),
            ('Snow Mold of Cereals', '''Symptoms:<br>''', 'Flowering'),
            ('Wheat Blast', '''Symptoms:<br>''', 'Flowering'),
            ('Take All', '''Symptoms:<br>''', 'Flowering'),
            ('Spider Mites', '''Symptoms:<br>''', 'Flowering'),
        ]
        for name, description, stage in wheat_diseases_flowering:
            disease = Disease(plant_id=wheat.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for wheat at the fruiting stage
        wheat_diseases_fruiting = [
            ('Karnal Bunt of Wheat', '''Symptoms:<br>''', 'Fruiting'),
            ('Loose Smut of Wheat', '''Symptoms:<br>''', 'Fruiting'),
            ('Fusarium Head Blight', '''Symptoms:<br>''', 'Fruiting'),
            ('Take All', '''Symptoms:<br>''', 'Fruiting'),
            ('Brown Stink Bug', '''Symptoms:<br>''', 'Fruiting'),
            ('Helicoberpa Capterpillar', '''Symptoms:<br>''', 'Fruiting'),
            ('Ear Cockle Eelworm', '''Symptoms:<br>''', 'Fruiting'),
        ]
        for name, description, stage in wheat_diseases_fruiting:
            disease = Disease(plant_id=wheat.id, name=name, description=description, stage=stage)
            db.session.add(disease)

        # Add disease data for wheat at the harvesting stage
        wheat_diseases_harvesting = [
            ('Loose Smut of Wheat', '''Symptoms:<br>''', 'Harvesting'),
            ('Fusarium Head Blight', '''Symptoms:<br>''', 'Harvesting'),
            ('Foot and Collar Rot', '''Symptoms:<br>''', 'Harvesting'),
            ('Fall Armuworm', '''Symptoms:<br>''', 'Harvesting'),
            ('Short horned Grasshopper and Locust', '''Symptoms:<br>''', 'Harvesting'),
            ('Frost Damage', '''Symptoms:<br>''', 'Harvesting'),

        ]
        for name, description, stage in wheat_diseases_harvesting:
            disease = Disease(plant_id=wheat.id, name=name, description=description, stage=stage)
            db.session.add(disease)


        db.session.commit()
        print("Data inserted successfully!")

if __name__ == '__main__':
    insert_data()
