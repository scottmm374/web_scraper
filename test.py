'''
Testing and checking results from one year prior to see how many events Im pulling and checking ID's as well to make sure numbers match up
Each is the print statements from Main.py for each URL tested.
'''

october = {'https://10times.com/salon-dela-photo', 'https://10times.com/epic-lille', 'https://10times.com/habitat-q', 'https://10times.com/nursing-congress-paris-france', 'https://10times.com/idc-european-cio-summit-vineuil-saint-firmin', 'https://10times.com/gcrse-paris', 'https://10times.com/pediatric-nursing-paris', 'https://10times.com/tokenomics-conference', 'https://10times.com/wine-spirits-summit', 'https://10times.com/mech-aero-paris', 'https://10times.com/catheter-ablation-techniques', 'https://10times.com/xcelerate-symphony-retail-forum', 'https://10times.com/trade-tech-france', 'https://10times.com/outsider-art-fair-paris', 'https://10times.com/forum-on-green-finance-and-investment-paris', 'https://10times.com/sfen-ath', 'https://10times.com/aic-interim-meeting-avignon', 'https://10times.com/euro-pharma-paris', 'https://10times.com/les-salons-du-mariage-albertville', 'https://10times.com/world-crypto-bitcoin-blockchain-and-cyber-security', 'https://10times.com/mobileone', 'https://10times.com/afcot-cotton-event-menton', 'https://10times.com/nursing-healthcare-paris', 'https://10times.com/international-colloquium-on-pediatrics-child-care', 'https://10times.com/hbpsurg', 'https://10times.com/qa-financial-forum-paris', 'https://10times.com/salon-wedding-tilques', 'https://10times.com/isscr-paris', 'https://10times.com/global-premier-congress-on-mental-health', 'https://10times.com/petit-strasbourg', 'https://10times.com/egg-paris-paris', 'https://10times.com/world-cancer-symposium', 'https://10times.com/comsol-conference-grenoble', 'https://10times.com/geong-forum-chamb-ry', 'https://10times.com/psd-paris', 'https://10times.com/collectionneurs', 'https://10times.com/computational-economics-and-finance', 'https://10times.com/iff-paris', 'https://10times.com/iccad-paris', 'https://10times.com/pci-ssc-europe-community-meeting', 'https://10times.com/habitat-immobilier-viving', 'https://10times.com/format-games', 'https://10times.com/iass-paris', 'https://10times.com/adaptive-nice', 'https://10times.com/salon-dauphinois', 'https://10times.com/gynecology-lle-de-france', 'https://10times.com/mondial-du-tatouage', 'https://10times.com/midwifery-paris', 'https://10times.com/euro-oncology', 'https://10times.com/wpnc-paris', 'https://10times.com/robot-manufacturing', 'https://10times.com/european-edition-sustainable', 'https://10times.com/aoac-europe-asfilab-symposium-paris', 'https://10times.com/idcreatives-clermont-ferrand', 'https://10times.com/artery-conference-nancy', 'https://10times.com/ieee-bmsb-issy-les-moulineaux', 'https://10times.com/lesalon-desmicro-enterprises', 'https://10times.com/nof-talence', 'https://10times.com/western-customer-relation-fair-nantes', 'https://10times.com/usf-convention-bordeaux', 'https://10times.com/top-recruitment', 'https://10times.com/pdt-pdd-symposium', 'https://10times.com/salon-du-tourisme-et-des-loisirs-de-pleine-nature', 'https://10times.com/conference-on-statistics-for-sustainable-finance', 'https://10times.com/euro-chemistry-congress-paris', 'https://10times.com/ycam-forum-toulouse', 'https://10times.com/nice-nice', 'https://10times.com/isc-malta', 'https://10times.com/wincom-reims', 'https://10times.com/retmo', 'https://10times.com/kyriba-live-treasury-finance-summit-paris', 'https://10times.com/salon-vindefrance-perantignet', 'https://10times.com/aal-forum-nice', 'https://10times.com/alphavisa', 'https://10times.com/international-conference-on-bioinspired-and-biobased-chemistry-materials', 'https://10times.com/tedx-alsac', 'https://10times.com/applying-eu-anti-discrimination-law-seminar-paris', 'https://10times.com/c-l', 'https://10times.com/ecio-nice', 'https://10times.com/longevity-troyes', 'https://10times.com/nephrology-paris', 'https://10times.com/inpho-venture-summit-bordeaux', 'https://10times.com/big-data-data-mining-and-machine-learni', 'https://10times.com/ces-europe-paris', 'https://10times.com/now-at-work-paris-paris', 'https://10times.com/household-personal-care', 'https://10times.com/acdl', 'https://10times.com/qvs-paris', 'https://10times.com/devfesttoulouse', 'https://10times.com/wusata-pavilion-at-sial-paris', 'https://10times.com/sp-aix-les-bains', 'https://10times.com/sustainable-brands-paris', 'https://10times.com/euro-clinical-obesity-and-diabetes-congress', 'https://10times.com/exhibition-artistic-training', 'https://10times.com/health-and-independence-trade-shows', 'https://10times.com/dynamic-spectrum-alliance-global-summit', 'https://10times.com/eventime-group-dev', 'https://10times.com/paris-motor-show', 'https://10times.com/ects-congress-marseille', 'https://10times.com/gazelec-congress', 'https://10times.com/vorticity-rotation-and-symmetry-marseille', 'https://10times.com/abmem', 'https://10times.com/gastroenterology-congress-paris', 'https://10times.com/ihrm-conference-paris', 'https://10times.com/paris-games-week', 'https://10times.com/ark-pediatrics-paris', 'https://10times.com/travel-mobility-days', 'https://10times.com/automation-class-factory-lyon-lyon', 'https://10times.com/karrass-effective-negotiating-seminar-paris', 'https://10times.com/epimar-montpellier', 'https://10times.com/european-ophthalmology-conference-paris', 'https://10times.com/icaps-nancy', 'https://10times.com/pathology-congress-paris', 'https://10times.com/global-experts-meeting-on-frontiers-in', 'https://10times.com/francece-auvergne-rhone-alpes'}

october_id = {'2849', '158796', '319364', '275119', '469733', '461972', '469443', '479532', '467295', '455588', '134779', '352233', '409602', '169357', '42724', '439370', '414212', '393848', '471936', '463069', '450500', '275978', '464983', '341718', '420654', '444264', '461986', '446096', '373123', '426802', '445230', '481700', '441459', '459802', '443900', '476739', '456841', '455630', '469796', '406259', '395554', '143391', '412417', '169513', '356155', '465586', '489004', '300683', '452351', '464763', '397552', '452755', '463663', '449517', '494793', '483235', '376316', '129158', '7099', '56965', '469124', '430746', '463082', '170242', '476573', '443291', '456639', '385122', '447438', '459004', '494775', '470788', '480877', '450460', '266820', '149885', '56128', '479957', '467640', '77515', '77888', '466234', '466227', '485396', '475801', '414787', '432742', '406531', '308059', '450255', '463631', '454192', '342729', '463961', '436031', '423243', '454654', '237074', '475820', '102012', '488796', '48676', '461971', '390806', '218364', '114298', '452280', '475587', '431147', '454972', '483231', '407911', '175958', '477219', '470972'}

nov = {'https://10times.com/gourmand', 'https://10times.com/dynamicspower-paris', 'https://10times.com/annual-meeting-chief-digital-officer', 'https://10times.com/value-chain-parts-lyon', 'https://10times.com/antiques-fair-nimes', 'https://10times.com/fair-havre', 'https://10times.com/run-digital-operations-lyon', 'https://10times.com/biennale', 'https://10times.com/creativa-montpellier', 'https://10times.com/skin-meeting', 'https://10times.com/emerging-materials-paris', 'https://10times.com/student-saint-etienne', 'https://10times.com/wedding-fair-and-festival-days-mans', 'https://10times.com/world-congress-on-pharmaceutics-and-novel-drug', 'https://10times.com/salon-du-mariage-le-mans', 'https://10times.com/ctn-paris', 'https://10times.com/salon-letudiant', 'https://10times.com/automation-class-factory-paris-paris', 'https://10times.com/salon-du-chocolat-et-gourmandises', 'https://10times.com/studyramafrance', 'https://10times.com/viving-lyon', 'https://10times.com/global-forum-on-competition', 'https://10times.com/go-study-abroad', 'https://10times.com/tficnanosafe', 'https://10times.com/annual-conference-innovation-and-prospective', 'https://10times.com/techshow', 'https://10times.com/eacta-annual-congress-grenoble', 'https://10times.com/festival-lights', 'https://10times.com/powering-growth', 'https://10times.com/national-conference-of-the-digital-humanities', 'https://10times.com/idcreatives-clermont-ferrand', 'https://10times.com/gastronomy-expo-troyes', 'https://10times.com/atcx-automobile-paris', 'https://10times.com/i-esa-tarbes', 'https://10times.com/faulkner-international-conference-besan-on', 'https://10times.com/copd-france', 'https://10times.com/devfesttoulouse', 'https://10times.com/gynecology-scientex', 'https://10times.com/student-fair-caen', 'https://10times.com/stem-cells-paris', 'https://10times.com/bioengineering-paris', 'https://10times.com/nutrition-conference-paris', 'https://10times.com/expo-meet-on-traditional-alternative-medicine', 'https://10times.com/nafems-france', 'https://10times.com/foliation-theory-and-complex-geometry-conference', 'https://10times.com/nantes-school-students', 'https://10times.com/psychiatry-paris', 'https://10times.com/production-temps-reel-strasbourg', 'https://10times.com/virtuality-fair', 'https://10times.com/housing-fair-nevers', 'https://10times.com/euro-heart-cardiology-conference-paris', 'https://10times.com/fotofever-paris', 'https://10times.com/hsconf-paris', 'https://10times.com/jdp-dermatological-congress-paris', 'https://10times.com/studyrama-quimper', 'https://10times.com/build-connect', 'https://10times.com/salon-de-l-etudiant', 'https://10times.com/international-symposium-institute-hand', 'https://10times.com/luxembourg-for-finance-conference-paris', 'https://10times.com/infer-research', 'https://10times.com/icmetl', 'https://10times.com/agrico-paris', 'https://10times.com/digital-humanities-and-digital-studies', 'https://10times.com/naturellia-expo-france', 'https://10times.com/mariage-le-mans', 'https://10times.com/salon-du-mariage-lille', 'https://10times.com/sofa-symposium', 'https://10times.com/eicc-rennes', 'https://10times.com/psychiatry-france', 'https://10times.com/new-frontiers-antitrust-conference', 'https://10times.com/e10s-rr3h-kh32', 'https://10times.com/delissime-limoges', 'https://10times.com/ipta', 'https://10times.com/mariage-de-clermont', 'https://10times.com/nanotechnology-paris', 'https://10times.com/global-experts-meet-on-dermatology', 'https://10times.com/studyrama-tours', 'https://10times.com/restconf-paris', 'https://10times.com/salon-dela-photo', 'https://10times.com/le-salon-de-l-etudiant', 'https://10times.com/congress-of-languedoc-roussillon-montpellier', 'https://10times.com/wedding-nantes', 'https://10times.com/salon-des-createurs-bordeaux', 'https://10times.com/international-conference-on-food-and-nutrition', 'https://10times.com/salon-dumariage', 'https://10times.com/public-health-paris', 'https://10times.com/wine-spirits-summit', 'https://10times.com/hbpsurg', 'https://10times.com/gcclforum'}
nov_id= {'475305', '484501', '494473', '456954', '78088', '474377', '487559', '445989', '465722', '457146', '451367', '485448', '311413', '469695', '17119', '446019', '177108', '478829', '463178', '75885', '454501', '77322', '255550', '463653', '452788', '132254', '305975', '487561', '324452', '463188', '53148', '42001', '441909', '444440', '177099', '254549', '77325', '170134', '70576', '425834', '461201', '77513', '177451', '100135', '472814', '440880', '210564', '431147', '78094', '353304', '521035', '164316', '2849', '308057', '247967', '465725', '485633', '48676', '311486', '13570', '373188', '348269', '126429', '390907', '77324', '463144', '481719', '169182', '447438', '429225', '345220', '452864', '463536', '485415', '458074', '485442', '458187', '224507', '437647', '375137', '385122', '69472', '452838', '144376', '329909', '450091', '577282', '146496', '474342'}

dec = {'https://10times.com/annual-conference-anti-corruption-fight', 'https://10times.com/imbioc-ieee', 'https://10times.com/festival-lights', 'https://10times.com/global-food-security-montpellier', 'https://10times.com/sfa-france', 'https://10times.com/antiques-fair-nimes', 'https://10times.com/macrotrend-conference-on-social-sciences', 'https://10times.com/run-digital-operations', 'https://10times.com/annual-international-yeats-society-conference', 'https://10times.com/isbm-lyon', 'https://10times.com/cofrend-days-congress', 'https://10times.com/pont-france', 'https://10times.com/health-social-medical', 'https://10times.com/sourcesuppliersshow', 'https://10times.com/infer-annual-conference-villetaneuse', 'https://10times.com/civ-world-conference', 'https://10times.com/biennale', 'https://10times.com/eeasa-poitiers', 'https://10times.com/world-congress-of-science-and-factual-producers', 'https://10times.com/gala-mayenne', 'https://10times.com/an-acoustic-market-lyon', 'https://10times.com/e1s0-r5zx-5g2z', 'https://10times.com/e1s4-94p4-kxrx', 'https://10times.com/medfit-conference-lille', 'https://10times.com/epic-meeting-on-micro-leds', 'https://10times.com/etsi-future-mobile'}
dec_id = {'440502', '463628', '465728', '247967', '468559', '77321', '474345', '405437', '428690', '400296', '398406', '75885', '447900', '452788', '424360', '443605', '438861', '453310', '105844', '548979', '425290', '341994', '475078', '487187', '576936', '382188'}

jan = {'https://10times.com/language-cultural-and-thematic-trips', 'https://10times.com/e1sx-h55p-d25f', 'https://10times.com/images-digital-summit', 'https://10times.com/piforum', 'https://10times.com/esi-forum-paris', 'https://10times.com/salon-des-formations', 'https://10times.com/shawls-scarves-paris', 'https://10times.com/cam-therapies', 'https://10times.com/mariage-fete-pau', 'https://10times.com/lyceen-student-bordeaux', 'https://10times.com/e1sx-d17d-0gx3', 'https://10times.com/pits-sia-congress', 'https://10times.com/isopt-paris', 'https://10times.com/pursuit-studies-and-masters-nancy', 'https://10times.com/cacvs-conference', 'https://10times.com/icc-international-mediation', 'https://10times.com/africa-ifa', 'https://10times.com/cacvs', 'https://10times.com/predictive-maintenance', 'https://10times.com/higher-education-montpellier', 'https://10times.com/mathematical-aspects-physics-with-non-self', 'https://10times.com/paris-student-fair', 'https://10times.com/vivez-nature-paris', 'https://10times.com/student-fair-versailles', 'https://10times.com/highschool-student-marseille', 'https://10times.com/global-sports-week', 'https://10times.com/lessons-learned-from-art-litigation-paris', 'https://10times.com/edhec-recruitment-fair', 'https://10times.com/student-subscribe-lyon', 'https://10times.com/otolaryngology-conference-paris', 'https://10times.com/student-fair-rouen', 'https://10times.com/nutr-event', 'https://10times.com/pgd-o', 'https://10times.com/student-fair-arras'}
jan_id = {'420612', '592410', '343135', '77331', '223884', '462736', '270817', '347907', '475024', '77328', '322551', '465689', '335307', '484954', '488612', '452673', '77326', '322525', '57994', '205887', '43459', '77443', '450624', '100963', '77446', '403523', '457903', '73782', '74046', '329346', '72232', '412672', '591139', '257600'}

feb= {'https://10times.com/securi-days', 'https://10times.com/e14s-xghd-0f29', 'https://10times.com/arci-conference', 'https://10times.com/rfl', 'https://10times.com/world-premier-heart-congress-paris', 'https://10times.com/efqm-forum-lyon', 'https://10times.com/salon-du-vegetal-nantes', 'https://10times.com/sfnp', 'https://10times.com/e1sz-164f-6phz', 'https://10times.com/cam-therapies', 'https://10times.com/paris-student-fair', 'https://10times.com/e1sk-p3g9-d4s2', 'https://10times.com/rubbercon-paris', 'https://10times.com/icpermed', 'https://10times.com/icc-international-mediation', 'https://10times.com/beauty-selection-nantes', 'https://10times.com/young-research-fellow-meeting', 'https://10times.com/pursuit-of-studies', 'https://10times.com/agricultural-show', 'https://10times.com/tranoi-preview', 'https://10times.com/wwm-global'}
feb_id = {'425684', '593210', '560426', '584315', '307939', '533254', '343135', '460487', '343893', '100963', '474347', '449905', '376314', '15412', '194954', '461985', '208738', '462736', '358725', '71705', '268810'}

mar = {'https://10times.com/techinnov', 'https://10times.com/isco-antibes', 'https://10times.com/e1s2-536x-hpkx', 'https://10times.com/aija-insol-europe-winter-seminar', 'https://10times.com/ink-the-sun', 'https://10times.com/hip-meets-spine-annual-conference-strasbourg', 'https://10times.com/iceps-conference-toulouse', 'https://10times.com/salon-des-vins-et-de-la-gastronomie-de-quimper', 'https://10times.com/new-architecture', 'https://10times.com/mrae-mar-cachan', 'https://10times.com/studyrama-training-france', 'https://10times.com/e1s5-5k30-hrhz', 'https://10times.com/salon-des-vins-et-de-la-gastronomie-de-vannes', 'https://10times.com/htcpm-symposium-antibes', 'https://10times.com/learning-alternation-marseille', 'https://10times.com/biomedical-photonics', 'https://10times.com/room-learning-lyon', 'https://10times.com/e1sk-5915-kszk', 'https://10times.com/security-printers-lyon', 'https://10times.com/medmun-conference', 'https://10times.com/biogaz-europe-expo', 'https://10times.com/e1s1-9x13-hkxk', 'https://10times.com/chemistry-nature-and-life-sciences', 'https://10times.com/salon-habitat-auxerre', 'https://10times.com/private-wealth-europe-forum', 'https://10times.com/tolexpo-lyon', 'https://10times.com/agricultural-show', 'https://10times.com/paris-hepatitis', 'https://10times.com/education-fair-toulouse', 'https://10times.com/e1sp-z5p3-p58r', 'https://10times.com/salon-du-livre-ancien-paris', 'https://10times.com/higher-education-rennes', 'https://10times.com/congress-sia-vision', 'https://10times.com/new-frontiers-in-digital-health-meeting', 'https://10times.com/sfpmed-annual-congress', 'https://10times.com/e1s0-x5g1-z8fr', 'https://10times.com/e133-sxh2-kfd4', 'https://10times.com/tranoi-preview', 'https://10times.com/international-symposium-on-work-in-agriculture', 'https://10times.com/pursuit-studies-and-masters', 'https://10times.com/e104-zfd4-xgg4', 'https://10times.com/e14s-pr7h-kd23', 'https://10times.com/motor-festival-avignon', 'https://10times.com/e1sk-28xs-46xf'}
mar_id = {'51966', '169310', '417607', '589590', '601933', '322550', '181670', '152757', '588568', '456033', '372237', '469118', '15333', '294335', '392054', '322565', '15412', '77517', '582726', '592801', '55669', '116580', '484892', '195285', '593607', '482903', '383707', '372482', '458367', '77523', '439333', '307868', '456108', '592898', '322524', '467599', '546447', '169345', '547281', '457682', '71705', '416495', '343236', '592489'}

apr = {'https://10times.com/e151-skhx-rd17', 'https://10times.com/e1s3-3r0r-4dfd', 'https://10times.com/e1sk-p0zs-6d07', 'https://10times.com/af-aerodynamics', 'https://10times.com/ifatcc-congress-roubaix', 'https://10times.com/international-conference-on-neurology-and-brain-d', 'https://10times.com/joint-meeting-of-isa-and-esa-issy-les-moulineaux', 'https://10times.com/eubce-marseille', 'https://10times.com/intermag-conference-lyon', 'https://10times.com/world-concrete-europe', 'https://10times.com/e1s0-r6r0-4gkf', 'https://10times.com/icsse-marseille', 'https://10times.com/bsg-paris', 'https://10times.com/e1s0-z1z2-h6hd', 'https://10times.com/creativa-metz', 'https://10times.com/e1s2-p6s1-0sgr', 'https://10times.com/e129-szks-ph21', 'https://10times.com/e13s-zxp1-xs03', 'https://10times.com/weurman-flavour-research-symposium-dijon', 'https://10times.com/apcm-europe', 'https://10times.com/ceva', 'https://10times.com/icc-european-conference-on-international-arbitrati', 'https://10times.com/interprofessional-refrigeration-and-its-applicatio', 'https://10times.com/fips-world-ski-patrol-congress-saint-bon-tarentais', 'https://10times.com/e1zf-zk04-z2h9', 'https://10times.com/echc-rouen', 'https://10times.com/e129-zfdf-z3p8', 'https://10times.com/iccie-paris', 'https://10times.com/e1s3-2p2r-8zfr', 'https://10times.com/euroneuro-congress', 'https://10times.com/cidr-expo-caen', 'https://10times.com/ehlers-danlos-society-european-learning-conference', 'https://10times.com/mipdoc', 'https://10times.com/carrefour-des-gestions-locales-de-leau', 'https://10times.com/rdd-nice', 'https://10times.com/mip-formats', 'https://10times.com/tlbs', 'https://10times.com/value-creation-for-owners-and-directors-fontaine'}
apr_id = {'440440', '386523', '547607', '17117', '114783', '569495', '488879', '606862', '545537', '351984', '474396', '568542', '566221', '116910', '475521', '459311', '247590', '466256', '470579', '254554', '443347', '584651', '438573', '412247', '160846', '3558', '582971', '427799', '424791', '601064', '149884', '457916', '577380', '432140', '457138', '360826', '444507', '577101'}

may = {'https://10times.com/west-industries-show', 'https://10times.com/e1z4-f6d0-x6kg', 'https://10times.com/salon-habitat-deco', 'https://10times.com/habitat-immobilier-nature-et-decoration', 'https://10times.com/iaea-nice', 'https://10times.com/entreprendre', 'https://10times.com/salon-vivre-cotesud', 'https://10times.com/wcgws', 'https://10times.com/wcms-paris', 'https://10times.com/foires-de-champagne', 'https://10times.com/international-symposium-on-auriculotherapy', 'https://10times.com/france-ce-caen', 'https://10times.com/crispr-meeting-paris', 'https://10times.com/fud', 'https://10times.com/annual-conference-csr-director', 'https://10times.com/paris-container-day', 'https://10times.com/e1s5-k2ks-1z6h', 'https://10times.com/foire-exposition-dangers2015', 'https://10times.com/e1sg-17x0-k3rs', 'https://10times.com/agriculture-and-horticulture-united-kingdom', 'https://10times.com/diana', 'https://10times.com/e1zf-21f5-x6rd', 'https://10times.com/international-conference-on-gynecology-and', 'https://10times.com/wcst-tokyo', 'https://10times.com/rdd-nice', 'https://10times.com/cebap-cachan', 'https://10times.com/devopsrex', 'https://10times.com/e1s0-11r1-rzkx', 'https://10times.com/afc-congress-paris', 'https://10times.com/affi-nantes', 'https://10times.com/e1zf-182h-z8zd', 'https://10times.com/iufro-division-risk-analysis-nancy', 'https://10times.com/dentist-expo', 'https://10times.com/e1zf-0xd8-h3z9', 'https://10times.com/echocardiography-cardiovascular', 'https://10times.com/e1s0-x6r3-7fdd', 'https://10times.com/e1s0-9r04-kkrz', 'https://10times.com/e1s3-4x28-sfkx', 'https://10times.com/europropre-expo', 'https://10times.com/international-conference-on-paris', 'https://10times.com/minalogic-business-meeting-lyon', 'https://10times.com/e1zf-x33h-3fh6', 'https://10times.com/frenchsocietyophthalmology', 'https://10times.com/e1s3-55k5-kgps', 'https://10times.com/e1s5-5p17-zzdk', 'https://10times.com/e13s-zxp1-xs03', 'https://10times.com/sf-m-congress-paris', 'https://10times.com/isev-annual-meeting-lyon', 'https://10times.com/scilifelab-the-svedberg-seminar-gif-sur-yvette', 'https://10times.com/carrefour-des-gestions-locales-de-leau', 'https://10times.com/annual-meeting-cervical-spine-research-society-', 'https://10times.com/ceva', 'https://10times.com/e1zf-h50z-2hh2', 'https://10times.com/bloody-week-end', 'https://10times.com/salonsce-tours', 'https://10times.com/weurman-flavour-research-symposium-dijon', 'https://10times.com/evdf', 'https://10times.com/reacteurope', 'https://10times.com/fair-for-grass-and-fodder-poussay', 'https://10times.com/france-ce', 'https://10times.com/e10s-kdfg-7s57', 'https://10times.com/carrefour-mayors-auvergne', 'https://10times.com/e1sr-z434-xrr5', 'https://10times.com/ufi-forum-on-sustainable-development'}
may_id = {'576977', '428851', '73344', '314448', '320363', '475066', '375604', '143646', '307700', '520601', '468155', '546618', '328834', '410380', '160846', '600971', '597011', '383473', '433243', '455677', '57993', '475521', '577689', '145367', '360826', '405998', '539875', '486623', '609202', '18349', '581035', '465680', '609126', '578876', '8790', '569495', '225472', '602661', '588562', '475630', '435079', '199082', '435896', '455675', '454015', '471273', '601983', '329609', '426827', '301568', '455575', '595089', '457543', '179557', '462536', '182050', '482848', '588345', '443665', '470668', '520597', '602622', '478860', '114783'}

jun = {'https://10times.com/e11z-ffx1-zz09', 'https://10times.com/urban-art-fair', 'https://10times.com/materials-energy', 'https://10times.com/global-paris', 'https://10times.com/mice-place-marseille', 'https://10times.com/energy-class-factory-france', 'https://10times.com/positive-psychology-in-practice-conference-paris', 'https://10times.com/mmin-lyon', 'https://10times.com/isos-toulouse', 'https://10times.com/biannual-conference-montpellier', 'https://10times.com/sepem-iindustries-est', 'https://10times.com/the-european-series-summit', 'https://10times.com/e1z3-9f28-zdzh', 'https://10times.com/e1s0-x3h1-k0gg', 'https://10times.com/e1s0-64s6-xhpf', 'https://10times.com/age3-tradefair', 'https://10times.com/rsbmh-cachan', 'https://10times.com/dataxday', 'https://10times.com/e1zd-gf38-z20s', 'https://10times.com/e1sr-s5x4-x0d1', 'https://10times.com/e1zf-55s2-xs2f', 'https://10times.com/salon-habitat-deco', 'https://10times.com/e1s1-r4s4-h1zk', 'https://10times.com/e1zh-z001-9rrd', 'https://10times.com/geoenergydays', 'https://10times.com/e1sr-12s4-3hgg', 'https://10times.com/e1zf-5p4s-r2f5', 'https://10times.com/bistops', 'https://10times.com/foire-exposition-dangers2015', 'https://10times.com/bim-world-paris', 'https://10times.com/e1s1-11k0-hddr', 'https://10times.com/production-temps-reel-lyon', 'https://10times.com/the-comatia-conference', 'https://10times.com/e1sx-3922-fsxf', 'https://10times.com/e1ss-364g-z5dd', 'https://10times.com/econometrics-games-matching-and-networks', 'https://10times.com/mvs-cannes', 'https://10times.com/e14s-kdr5-fd07', 'https://10times.com/phc-clichy', 'https://10times.com/e1z4-f9r3-k0pf', 'https://10times.com/icppnice', 'https://10times.com/e1zf-p2r4-d42f', 'https://10times.com/avantex-paris', 'https://10times.com/foires-de-champagne', 'https://10times.com/blendwebmix', 'https://10times.com/international-symposium-on-auriculotherapy', 'https://10times.com/e1s4-k8x3-s8sg', 'https://10times.com/ijcar-aubervilliers', 'https://10times.com/e1sk-0xz7-z42z', 'https://10times.com/e1ss-3g6z-3d8f', 'https://10times.com/cnge-congress-bordeaux', 'https://10times.com/icoria-bordeaux', 'https://10times.com/surcar2015', 'https://10times.com/petit-lyon', 'https://10times.com/preventica-lyon', 'https://10times.com/robocup-exhibition-bordeaux', 'https://10times.com/pediatric-dermatology-seminar', 'https://10times.com/aiscongress', 'https://10times.com/e15s-kgh1-p2z0', 'https://10times.com/international-multidisciplinary-academic', 'https://10times.com/aawmconference', 'https://10times.com/e1s5-s7g3-sk7d', 'https://10times.com/e1z5-h9x1-s3sh', 'https://10times.com/apparel-sourcing-paris', 'https://10times.com/global-premier-congress-on-women-health', 'https://10times.com/salon-vivre-cotesud', 'https://10times.com/aciek-academy', 'https://10times.com/e1s0-x5x1-d4ff', 'https://10times.com/production-temps-reel-lille', 'https://10times.com/e1sr-2h7f-0g8s', 'https://10times.com/anti-corruption-north-africa', 'https://10times.com/esat-paris', 'https://10times.com/habitat-immobilier-nature-et-decoration', 'https://10times.com/congress-sfnr', 'https://10times.com/e1z5-83f0-fxsx', 'https://10times.com/le-salon-baby-france', 'https://10times.com/compas-lyon', 'https://10times.com/pi-seminar-paris', 'https://10times.com/iaee-paris', 'https://10times.com/e1z1-d4f0-r2rr', 'https://10times.com/agrivoltaics-conference', 'https://10times.com/btec-annual-conference'}
jun_id = {'629552', '424974', '559240', '480882', '477938', '582117', '355610', '581701', '392034', '479413', '451376', '468508', '475306', '240925', '443661', '265263', '483891', '412000', '506927', '553581', '525958', '476390', '312725', '57993', '73566', '320363', '592833', '196884', '604710', '590590', '132299', '448659', '56281', '127873', '407512', '553610', '600959', '132547', '599100', '420887', '410205', '606162', '457397', '72345', '185242', '589553', '472012', '469390', '472983', '553611', '403946', '517556', '613065', '575991', '41741', '575233', '454500', '472942', '443051', '351708', '607840', '583246', '605950', '376315', '575268', '604570', '409002', '199082', '475303', '626771', '410380', '470691', '600966', '179557', '572035', '461987', '589666', '58882', '30195', '610777', '484485', '145367'}

jul = {'https://10times.com/e14z-fxg3-f1h0', 'https://10times.com/secrypt-lieusaint', 'https://10times.com/e1zf-30zd-2x3h', 'https://10times.com/european-meeting-on-glial-cells-in-health-and', 'https://10times.com/e1z4-144g-rdhx', 'https://10times.com/simultech-lieusaint', 'https://10times.com/cannes-international-film-festival', 'https://10times.com/itsis-paris', 'https://10times.com/e13s-zkzf-5h42', 'https://10times.com/avantex-paris', 'https://10times.com/rict-bordeaux', 'https://10times.com/ethcc-paris', 'https://10times.com/petit-nantes', 'https://10times.com/icsb-world-congress-paris', 'https://10times.com/asset-management-summit-paris', 'https://10times.com/e1sx-3922-fsxf', 'https://10times.com/eacmfs-events', 'https://10times.com/e1sr-x261-2dfd', 'https://10times.com/icinco-lieusaint', 'https://10times.com/dataconference', 'https://10times.com/bistops', 'https://10times.com/ice-b-lieusaint', 'https://10times.com/fbc-nancy', 'https://10times.com/winsys-lieusaint', 'https://10times.com/e145-skfx-rr27', 'https://10times.com/etelemed', 'https://10times.com/richard-aldington-imagism-conference', 'https://10times.com/mice-place-marseille', 'https://10times.com/international-conference-on-cultural', 'https://10times.com/e1ss-465d-3rpr', 'https://10times.com/sigmap-lieusaint', 'https://10times.com/bekm-cachan', 'https://10times.com/e1z4-f9r3-k0pf', 'https://10times.com/icsoft-lieusaint', 'https://10times.com/iarmea-paris', 'https://10times.com/esat-paris', 'https://10times.com/compas-lyon', 'https://10times.com/fib-international-phd-symposium-in-civil-engineeri', 'https://10times.com/iscb-lyon', 'https://10times.com/e1s0-9k3h-8rdf', 'https://10times.com/iaee-paris', 'https://10times.com/e1z4-h3p0-g1rk', 'https://10times.com/apparel-sourcing-paris', 'https://10times.com/ijcar-aubervilliers', 'https://10times.com/isos-toulouse', 'https://10times.com/e1sr-x35d-f1g2', 'https://10times.com/delta-lieusaint'}
jul_id = {'485755', '72344', '590590', '580977', '483891', '472012', '551747', '456622', '412000', '440666', '383246', '430151', '579103', '606192', '430013', '446578', '420887', '472127', '579101', '430150', '474972', '312725', '429277', '460755', '440097', '637129', '624378', '267205', '423265', '430050', '568602', '448929', '415021', '609302', '453271', '430044', '429276', '57509', '463207', '484485', '454500', '376315', '607840', '582710', '488137', '30195', '430039'}

aug = {'https://10times.com/e1z4-6f4s-9fds', 'https://10times.com/understanding-voluntary-and-forced-migration', 'https://10times.com/aab-legume-science-and-practice-angers', 'https://10times.com/le-cabaret-vert', 'https://10times.com/interfiliere-paris', 'https://10times.com/e1s2-r6d1-f2zz', 'https://10times.com/e1s4-r8r3-d9dk', 'https://10times.com/e1s5-31r9-rddx', 'https://10times.com/hyp-conference-lyon', 'https://10times.com/eappc-beams', 'https://10times.com/asa-hitran', 'https://10times.com/antiquaires-vintage', 'https://10times.com/esse-lyon', 'https://10times.com/ihiet-paris', 'https://10times.com/salon-des-vins-et-de-la-gastronomie-de-biarritz', 'https://10times.com/near-surface-geoscience-conference-exhibition', 'https://10times.com/e1s1-01z5-fsgs', 'https://10times.com/e1zf-hx35-rs39', 'https://10times.com/international-foire-europeenne', 'https://10times.com/aaate-conference-paris', 'https://10times.com/ats-paris', 'https://10times.com/e1zp-r49x-d24k', 'https://10times.com/e1s3-x1fh-1dz5', 'https://10times.com/studyrama-rentree-etudiante', 'https://10times.com/e14z-zzr9-gg47', 'https://10times.com/congress-aesthetic-medicine-and-dermatological', 'https://10times.com/e1zd-5927-fgdf', 'https://10times.com/e1sk-s55r-2rx5', 'https://10times.com/e1ss-r08s-44gr', 'https://10times.com/art-o-rama', 'https://10times.com/world-conservation-congress-marseille', 'https://10times.com/dynamicsdays-nice', 'https://10times.com/e10s-srsg-z636', 'https://10times.com/rebm-cachan', 'https://10times.com/e1ss-3653-kszp', 'https://10times.com/cezanne-tattoo-ink', 'https://10times.com/international-congress-on-epilepsy-paris', 'https://10times.com/e-ins-paris', 'https://10times.com/e11s-rpk5-kf46', 'https://10times.com/health-conference-paris', 'https://10times.com/e1zd-0s9h-0p1r'}
aug_id = {'557536', '416295', '557537', '610310', '284795', '533970', '8673', '370146', '560535', '449240', '398999', '242265', '426674', '605015', '466272', '455327', '425320', '48771', '462509', '577118', '440091', '361779', '647918', '577119', '615247', '53030', '585779', '276025', '590216', '571066', '558564', '481203', '463134', '666733', '602975', '169276', '574880', '264410', '445565', '101563', '475458'}

sep_first = {'https://10times.com/made-in-france', 'https://10times.com/francece-brest', 'https://10times.com/petit', 'https://10times.com/international-conference-on-frontiers-signal', 'https://10times.com/tattoo-convention-yu', 'https://10times.com/g-20y', 'https://10times.com/e11s-xsss-9g02', 'https://10times.com/webisland-nantes', 'https://10times.com/international-foire-europeenne', 'https://10times.com/devbreak-bouville', 'https://10times.com/eosam-paris', 'https://10times.com/e14z-zzr9-gg47', 'https://10times.com/national-exhibition-shellfish-and-marine-cultures', 'https://10times.com/industrie-expo', 'https://10times.com/e1zf-z57d-2k5f', 'https://10times.com/e1s2-22x6-hskx', 'https://10times.com/international-conference-on-neurology-neuro-disord', 'https://10times.com/hyp-conference-lyon', 'https://10times.com/salonsce-lyon', 'https://10times.com/salon-maisonpassion-villefranchesursaone', 'https://10times.com/medfit-conference-grenoble', 'https://10times.com/salonsce-montpellier', 'https://10times.com/salon-des-vins-et-de-la-gastronomie-de-lehavre', 'https://10times.com/simesitem-expo-paris', 'https://10times.com/world-conservation-congress-marseille', 'https://10times.com/le-salon-maison-de-cognac', 'https://10times.com/e1zf-hz4z-7x16', 'https://10times.com/itss-sep-cachan', 'https://10times.com/francece-nice', 'https://10times.com/e1zf-50h1-8dkr', 'https://10times.com/surgery-and-anaesthesia-paris', 'https://10times.com/salon-national', 'https://10times.com/salon-du-mariage-le', 'https://10times.com/e12z-psr3-p0r8', 'https://10times.com/fair-mans', 'https://10times.com/e1zf-32rz-1rh1', 'https://10times.com/fair-of-savoie', 'https://10times.com/salon-des-vins-et-de-la-gastronomie-de-biarritz', 'https://10times.com/e1zs-31h5-f2px', 'https://10times.com/immunorad', 'https://10times.com/art-o-rama', 'https://10times.com/esscirc-and-essderc-grenoble', 'https://10times.com/e12z-fd7x-ps00', 'https://10times.com/icsf', 'https://10times.com/e1sx-d51h-3s4h', 'https://10times.com/parish-aash-symposium', 'https://10times.com/ecoc-exhibition-bordeaux', 'https://10times.com/salon-auto-moto-classic-toulouse', 'https://10times.com/owc-rennes', 'https://10times.com/space-expo-rennes', 'https://10times.com/france-nancy', 'https://10times.com/edition-french-software-testing-day', 'https://10times.com/e1z1-z1z5-p3dx', 'https://10times.com/we-love-green', 'https://10times.com/omyague-expo-paris', 'https://10times.com/e1z4-f3rg-4sx1', 'https://10times.com/e1zp-10px-01zs', 'https://10times.com/e14z-pg1k-k4k2', 'https://10times.com/e1z5-52p7-pxzf', 'https://10times.com/innov-agri', 'https://10times.com/aftes-international-congress', 'https://10times.com/imog-montpellier'}
sep_first_id = {'481203', '18168', '666419', '209685', '378228', '455173', '334126', '602669', '645747', '487546', '276600', '44339', '42036', '607359', '592589', '595553', '319375', '64560', '207598', '468961', '356750', '388172', '644965', '485105', '601945', '473716', '652049', '370146', '41944', '339851', '353303', '73634', '644960', '301512', '458376', '145471', '301582', '314544', '334654', '426293', '446278', '21435', '591252', '424445', '666733', '169276', '340583', '5830', '370777', '52705', '101563', '8331', '606180', '607672', '434625', '643888', '416396', '50737', '48771', '276924', '602187', '169337'}

sep_second = {'https://10times.com/e14z-pk3s-3gx4', 'https://10times.com/e14z-fhz9-rf08', 'https://10times.com/industrial-analysis-exhibition', 'https://10times.com/immunorad', 'https://10times.com/europack-summit-monte-carlo', 'https://10times.com/e1zp-2z1r-3x2p', 'https://10times.com/performance-measurement-and-management-control', 'https://10times.com/cwc-paris', 'https://10times.com/e1s3-k7k0-z6pd', 'https://10times.com/immotissimo', 'https://10times.com/e1zf-32rz-1rh1', 'https://10times.com/space-expo-rennes', 'https://10times.com/salon-immotissimo', 'https://10times.com/medfit-conference-grenoble', 'https://10times.com/e13z-pp5f-kf24', 'https://10times.com/equipbaie-paris', 'https://10times.com/data-science-paris', 'https://10times.com/e135-2zgz-zxp5', 'https://10times.com/foire-de-pau', 'https://10times.com/esmo-congress-paris', 'https://10times.com/surgery-and-anaesthesia-paris', 'https://10times.com/world-congress-on-nursing-and-healthcare-paris', 'https://10times.com/e1s5-r4r0-g0rs', 'https://10times.com/e1zp-k06r-z3r1', 'https://10times.com/annual-meeting-european-congress-of-sotest', 'https://10times.com/iopc', 'https://10times.com/salonsce-reims', 'https://10times.com/e1sk-d055-g5fp', 'https://10times.com/e1zf-hzz3-41s7', 'https://10times.com/e1z2-8d0h-5zkh', 'https://10times.com/chimielyon', 'https://10times.com/cartoon-forum', 'https://10times.com/e1s4-7k29-sgrd', 'https://10times.com/salon-immobilier-perpignan', 'https://10times.com/sifem', 'https://10times.com/european-dysmorphology-meeting', 'https://10times.com/e1z3-0d0h-z3ks', 'https://10times.com/imog-montpellier', 'https://10times.com/geopolitics-and-economics-iot-ai-and-robotics', 'https://10times.com/e1zf-20kz-15dh', 'https://10times.com/packinnove', 'https://10times.com/simesitem-expo-paris', 'https://10times.com/netgcoop-carg-se', 'https://10times.com/school-of-po-the-conference-paris', 'https://10times.com/nantucket-island-fair', 'https://10times.com/e1zp-502k-z8dk', 'https://10times.com/copd-paris', 'https://10times.com/e1zs-43fg-59dp', 'https://10times.com/epn-paris', 'https://10times.com/e15z-pp6x-1zd6', 'https://10times.com/e1sr-04zd-5fd4', 'https://10times.com/national-exhibition-shellfish-and-marine-cultures', 'https://10times.com/salon-habitat-meubles-and-deco', 'https://10times.com/international-conference-on-neurology-neuro-disord', 'https://10times.com/egccc-paris', 'https://10times.com/salon-de-lhabitat-de-meaux', 'https://10times.com/salonsce-montpellier', 'https://10times.com/e1sk-57rf-1xr5', 'https://10times.com/aviation-paris', 'https://10times.com/e1zp-10px-01zs', 'https://10times.com/placemarketingforum', 'https://10times.com/e1z5-g5f1-g9pd', 'https://10times.com/e1z3-g3z1-g8dz', 'https://10times.com/salonsce-lyon', 'https://10times.com/ecoc-exhibition-bordeaux', 'https://10times.com/salon-national', 'https://10times.com/professional-showroom-dedicated-to-internet', 'https://10times.com/e1s2-44k5-zsdk', 'https://10times.com/francece-limoges', 'https://10times.com/salon-habitat-vitre', 'https://10times.com/seanergy-forum', 'https://10times.com/decielec-t', 'https://10times.com/le-cuir-a-paris', 'https://10times.com/salonsce-lille', 'https://10times.com/fdd-paris', 'https://10times.com/e1zf-50h1-8dkr', 'https://10times.com/icc-france', 'https://10times.com/eus-endo', 'https://10times.com/e11z-g8fs-5dg1', 'https://10times.com/taste-paris-france', 'https://10times.com/vrws-annecy', 'https://10times.com/fair-of-savoie', 'https://10times.com/e1s4-7k37-kggh', 'https://10times.com/sfm-nantes'}
sep_second_id = {'434625', '301570', '644080', '165049', '315649', '459320', '243786', '5175', '636694', '402918', '648767', '646794', '424445', '602665', '74810', '392543', '435986', '18167', '421632', '341298', '648539', '230285', '636316', '586518', '18230', '145471', '577375', '351163', '264129', '426293', '602187', '444929', '468961', '454961', '465165', '612685', '630341', '319833', '455173', '485097', '588641', '648618', '441128', '340583', '644965', '602670', '163254', '398577', '44339', '468626', '128062', '230883', '453390', '146768', '650314', '630513', '581304', '515267', '608612', '607672', '475050', '393548', '585371', '644961', '588332', '278748', '432772', '587097', '18375', '456258', '446739', '206007', '445658', '447760', '42036', '474770', '52705', '18168', '612682', '446278', '133669', '576101', '21435', '145462'}

sep_third = {'https://10times.com/grand-pavois-rochelle', 'https://10times.com/salon-maison-bois', 'https://10times.com/sfm-nantes', 'https://10times.com/e1zf-f03g-59fz', 'https://10times.com/decielec-t', 'https://10times.com/le-cuir-a-paris', 'https://10times.com/gpmb-paris', 'https://10times.com/build-your-house', 'https://10times.com/annual-conference-communication-director', 'https://10times.com/e14z-fhz9-rf08', 'https://10times.com/measurement-world-france', 'https://10times.com/iccnt-paris', 'https://10times.com/e1z5-2s0f-6rrk', 'https://10times.com/sirha-lyon', 'https://10times.com/e1s5-r4r0-g0rs', 'https://10times.com/e1zp-k06r-z3r1', 'https://10times.com/brains-paris', 'https://10times.com/e1zp-30xf-1r3g', 'https://10times.com/gcsa-france', 'https://10times.com/salon-de-l-habitat-rennes', 'https://10times.com/vannes-fair', 'https://10times.com/e1z3-854h-rzrk', 'https://10times.com/ai-net-conference', 'https://10times.com/preventica-north-france', 'https://10times.com/fair-wedding', 'https://10times.com/iopc', 'https://10times.com/geopolitics-and-economics-iot-ai-and-robotics', 'https://10times.com/aero-air-show', 'https://10times.com/eco-rock-festival-cabaret-vert', 'https://10times.com/salonbio-respirelavie-poitiers', 'https://10times.com/salonsce-paris', 'https://10times.com/industrial-analysis-exhibition', 'https://10times.com/e1z5-g5f1-g9pd', 'https://10times.com/e1sk-d055-g5fp', 'https://10times.com/retail-chain', 'https://10times.com/e10z-pxd3-ff29', 'https://10times.com/festisalonsl-ens', 'https://10times.com/netgcoop-carg-se', 'https://10times.com/e-health-university', 'https://10times.com/e1z1-h9p3-h2sh', 'https://10times.com/printemps-des-etudes', 'https://10times.com/e1z3-0d0h-z3ks', 'https://10times.com/foire-de-pau', 'https://10times.com/id-creatives-lyon', 'https://10times.com/professional-showroom-dedicated-to-internet', 'https://10times.com/e120-sppf-5gx1', 'https://10times.com/salon-alina-bordeaux', 'https://10times.com/sfen-npc', 'https://10times.com/devoxx-france', 'https://10times.com/leisure-vehicles-trade-show', 'https://10times.com/salonsce-strasbourg', 'https://10times.com/equipmag-expo', 'https://10times.com/silmo-optical-exhibition', 'https://10times.com/whisky-live-paris', 'https://10times.com/france-ce-annecy', 'https://10times.com/foireinternationale-saint-etienne', 'https://10times.com/international-meeting-on-ampk-vian-les-bains', 'https://10times.com/pour-lamour-du', 'https://10times.com/taste-paris-france', 'https://10times.com/global-lodging-forum', 'https://10times.com/e1s4-7k37-kggh', 'https://10times.com/petit-lille', 'https://10times.com/sfar-national-congress', 'https://10times.com/seanergy-forum', 'https://10times.com/salon-del-l-immobilier-mediterranee', 'https://10times.com/e1z2-41z4-rhpp', 'https://10times.com/icitt-paris', 'https://10times.com/equipbaie-paris', 'https://10times.com/mobilehci-toulouse', 'https://10times.com/e1sx-s14f-s5g9', 'https://10times.com/international-metrology-congress', 'https://10times.com/chimielyon', 'https://10times.com/european-dysmorphology-meeting', 'https://10times.com/world-congress-on-nursing-and-healthcare-paris', 'https://10times.com/cartoon-forum', 'https://10times.com/salon-desentrepreneurs', 'https://10times.com/big-data-paris-france', 'https://10times.com/annual-conference-e-health', 'https://10times.com/salon-maison', 'https://10times.com/e1s3-k7k0-z6pd', 'https://10times.com/e14z-fsk1-k4s3', 'https://10times.com/e13z-pp5f-kf24', 'https://10times.com/e1zf-hzz3-41s7', 'https://10times.com/e1s4-x2pz-5f8p', 'https://10times.com/copd-paris', 'https://10times.com/e1z2-8d0h-5zkh', 'https://10times.com/it-partners', 'https://10times.com/e1zs-43fg-59dp', 'https://10times.com/isga-nancy', 'https://10times.com/icdo-paris', 'https://10times.com/international-rare-book-and-autograph-fair', 'https://10times.com/ictm-paris', 'https://10times.com/ictm-france', 'https://10times.com/batteries-event-lyon', 'https://10times.com/e1z0-34r7-pdpk', 'https://10times.com/salon-habitat-dreux', 'https://10times.com/eiasm-conference', 'https://10times.com/e11z-g8fs-5dg1', 'https://10times.com/salon-des-vins-et-de-la-gastronomie-de', 'https://10times.com/e15z-zfz1-gf47', 'https://10times.com/annual-gar-live-construction-disputes-conference', 'https://10times.com/salonsce-nantes', 'https://10times.com/cat-paris', 'https://10times.com/e1zp-502k-z8dk', 'https://10times.com/e1s1-x8z0-p8gh', 'https://10times.com/foire-internationale-de-metz'}
sep_third_id = {'226487', '77802', '102182', '113392', '22134', '128062', '156867', '72347', '595053', '485097', '8722', '3654', '465165', '602670', '301569', '113630', '644080', '55862', '454875', '577375', '612685', '71697', '461015', '605885', '624252', '319026', '464648', '3733', '648618', '465700', '463364', '630341', '53029', '445727', '453619', '319833', '445589', '588641', '341298', '660630', '145460', '379419', '278748', '544039', '475503', '23393', '627678', '48675', '600306', '435986', '581304', '55838', '18172', '5834', '446010', '18230', '64476', '594604', '169246', '465684', '75913', '323702', '483984', '315130', '309487', '650314', '247972', '5175', '461875', '384062', '407749', '169270', '354687', '444929', '55790', '649073', '392543', '133669', '264129', '667244', '674148', '602665', '383426', '650778', '455698', '612682', '453893', '486888', '648767', '427301', '588332', '163254', '18192', '379754', '474770', '469818', '596432', '398577', '224571', '7727', '630513', '18173', '515267', '463363', '70980', '649100'}

sep_fourth = {'https://10times.com/gpmb-paris', 'https://10times.com/ifnane-paris', 'https://10times.com/e-achats', 'https://10times.com/miss-montpellier', 'https://10times.com/e1zz-3k7k-4hr0', 'https://10times.com/equipmag-expo', 'https://10times.com/forum-labo-biotech', 'https://10times.com/francece-poitiers', 'https://10times.com/e1sx-s14f-s5g9', 'https://10times.com/vannes-fair', 'https://10times.com/salon-habitatfontaine', 'https://10times.com/measurement-world-france', 'https://10times.com/e14z-g7xr-1ps5', 'https://10times.com/salonsce-rennes', 'https://10times.com/salon-studyrama', 'https://10times.com/e11z-sp3s-f2p9', 'https://10times.com/maison-esprit-jardin', 'https://10times.com/tranoi-paris', 'https://10times.com/international-meeting-on-ampk-vian-les-bains', 'https://10times.com/e-sm-marseille', 'https://10times.com/e1zg-1xs5-g4r4', 'https://10times.com/salon-zen', 'https://10times.com/leisure-vehicles-trade-show', 'https://10times.com/grand-pavois-rochelle', 'https://10times.com/e1zp-2sr8-p3k1', 'https://10times.com/ever', 'https://10times.com/summit-livestock', 'https://10times.com/e10z-p8rz-2zx1', 'https://10times.com/batteries-event-lyon', 'https://10times.com/e1s3-6k13-gdgf', 'https://10times.com/e1z2-41z4-rhpp', 'https://10times.com/pour-lamour-du', 'https://10times.com/globalinvestforum', 'https://10times.com/esope', 'https://10times.com/francece-amiens', 'https://10times.com/e1sx-fh32-56xd', 'https://10times.com/e1z0-34r7-pdpk', 'https://10times.com/vigne-gastronomie-strasbourg', 'https://10times.com/e1z5-p5p0-x0sk', 'https://10times.com/retail-days', 'https://10times.com/ai-net-conference', 'https://10times.com/brains-paris', 'https://10times.com/wedding-fair-aubagne', 'https://10times.com/serveurs-et-applications', 'https://10times.com/international-metrology-congress', 'https://10times.com/sfen-npc', 'https://10times.com/isga-nancy', 'https://10times.com/sfro', 'https://10times.com/kernel-recipes-paris', 'https://10times.com/e1zp-30xf-1r3g', 'https://10times.com/e11z-pz8d-kh12', 'https://10times.com/imedia-brand-summit-biarritz', 'https://10times.com/sdv', 'https://10times.com/e1z0-z0r4-7fgr', 'https://10times.com/family-enterprise-challenge', 'https://10times.com/e1s4-x2pz-5f8p', 'https://10times.com/preventica-north-france', 'https://10times.com/art-f-lyon', 'https://10times.com/cloud-computing-world-expo', 'https://10times.com/e1z1-h9p3-h2sh', 'https://10times.com/salonde-limmobilier-toulouse', 'https://10times.com/autonomic-grand-ouest', 'https://10times.com/e10z-pxd3-ff29', 'https://10times.com/mariage-et-du-pacs-strasbourg', 'https://10times.com/e1z1-6r5f-5xxk', 'https://10times.com/mariage-oriental-nimes', 'https://10times.com/mobilehci-toulouse', 'https://10times.com/e1z3-854h-rzrk', 'https://10times.com/e1s1-x8z0-p8gh', 'https://10times.com/it-partners', 'https://10times.com/the-box-paris', 'https://10times.com/e1z1-552r-fxxr', 'https://10times.com/congress-biocides', 'https://10times.com/itechmer-lorient', 'https://10times.com/novafleur', 'https://10times.com/habitat-expo-brest', 'https://10times.com/les-salons-du-mariage', 'https://10times.com/e1z5-2s0f-6rrk', 'https://10times.com/e1z1-f7h2-rs1r', 'https://10times.com/age3', 'https://10times.com/e1sp-3xp3-k1k2', 'https://10times.com/salon-des-seniors', 'https://10times.com/erp-asp', 'https://10times.com/salon-solutions-maison', 'https://10times.com/destination-habitat-annemasse2015', 'https://10times.com/animal-expo-paris', 'https://10times.com/devoxx-france', 'https://10times.com/euro-global-conference-on-food-science-an', 'https://10times.com/foireinternationale-saint-etienne', 'https://10times.com/e1z5-4r4s-4hdx', 'https://10times.com/salonsce-dijon', 'https://10times.com/iftm', 'https://10times.com/salon-alina-bordeaux', 'https://10times.com/salonsce-paris', 'https://10times.com/foire-internationale-de-metz', 'https://10times.com/e1s5-2s14-pfxs', 'https://10times.com/display', 'https://10times.com/salon-de-lhabitat-de-rochefort', 'https://10times.com/workspace-expo', 'https://10times.com/salon-des-vins-et-de-la-gastronomie-de-vertou', 'https://10times.com/immobilier-marcq-baroeul', 'https://10times.com/e1zp-5kz0-d22r', 'https://10times.com/symposium-on-hormones-and-cell-regulation', 'https://10times.com/e1sr-0rk8-k3x6', 'https://10times.com/energy-time', 'https://10times.com/grape-harvest-festival', 'https://10times.com/patrimonia'}
sep_fourth_id = {'51395', '169319', '18052', '301571', '549488', '434178', '5834', '668827', '18175', '60162', '583130', '18173', '170127', '438145', '427301', '648617', '77883', '654504', '77684', '674148', '64476', '602757', '139070', '301572', '55862', '453893', '624252', '204294', '304572', '145460', '675219', '483984', '331181', '476949', '596432', '77535', '645748', '23393', '230292', '384062', '203330', '445637', '650778', '7727', '376318', '554095', '323112', '667037', '8722', '590291', '48731', '577889', '383426', '445589', '56280', '56163', '639745', '247873', '33986', '235115', '649100', '18869', '594604', '595053', '226487', '649073', '52875', '379419', '454875', '73858', '71418', '20876', '670997', '639537', '647669', '21803', '310470', '316801', '646182', '271495', '267551', '75913', '439251', '342711', '486888', '50321', '264593', '375366', '644958', '667244', '74805', '670998', '18021', '189191', '183697', '101727', '469818', '379754', '1097', '183715', '461015', '270806', '404576', '627678', '144482', '319249', '410984'}
total = set()

print("<-------October Duplicates----------->")
for x in october:
    if x in total:
        print("Oct: " , x)
    total.add(x)
print("<-------November Duplicates----------->")
for x in nov:
    if x in total:
        print("Nov: " , x)
    total.add(x)
print("<-------December Duplicates----------->")
for x in dec:
    if x in total:
        print("Dec: " , x)
    total.add(x)
print("<-------January Duplicates----------->")
for x in jan:
    if x in total:
        print("Jan: " , x)
    total.add(x)
print("<-------February Duplicates----------->")
for x in feb:
    if x in total:
        print("Feb: " , x)
    total.add(x)
print("<-------March Duplicates----------->")
for x in mar:
    if x in total:
        print("Mar: " , x)
    total.add(x)
print("<-------April Duplicates----------->")
for x in apr:
    if x in total:
        print("Apr: " , x)
    total.add(x)
print("<-------May Duplicates----------->")
for x in may:
    if x in total:
        print("May: " , x)
    total.add(x)
print("<-------June Duplicates----------->")
for x in jun:
    if x in total:
        print("Jun: " , x)
    total.add(x)
print("<-------July Duplicates----------->")
for x in jul:
    if x in total:
        print("Jul: " , x)
    total.add(x)
print("<-------August Duplicates----------->")
for x in aug:
    if x in total:
        print("Aug: " , x)
    total.add(x)
print("<-------SEPTEMBER First Duplicates----------->")
for x in sep_first:
    if x in total:
        print("Sep First: ", x)
    total.add(x)

print("<-------SEPTEMBER Second Duplicates----------->")
for x in sep_second:
    if x in total:
        print("Sep Second : ", x)
    total.add(x)

print("<-------SEPTEMBER Third Duplicates----------->")
for x in sep_third:
    if x in total:
        print("Sep Third: ", x)
    total.add(x)

print("<-------SEPTEMBER Fourth Duplicates----------->")
for x in sep_fourth:
    if x in total:
        print("Sep Fourth: ", x)
    total.add(x)

id_total = set()

print("<-------October ID Duplicates----------->")
for x in october_id:
    if x in id_total:
        print("Oct: " , x)
    id_total.add(x)
print("<-------November ID Duplicates----------->")
for x in nov_id:
    if x in id_total:
        print("Nov: " , x)
    id_total.add(x)
print("<-------December ID Duplicates----------->")
for x in dec_id:
    if x in id_total:
        print("Dec: " , x)
    id_total.add(x)
print("<-------January ID Duplicates----------->")
for x in jan_id:
    if x in id_total:
        print("Jan: " , x)
    id_total.add(x)
print("<-------February ID Duplicates----------->")
for x in feb_id:
    if x in id_total:
        print("Feb: " , x)
    id_total.add(x)
print("<-------March ID Duplicates----------->")
for x in mar_id:
    if x in id_total:
        print("Mar: " , x)
    id_total.add(x)
print("<-------April ID Duplicates----------->")
for x in apr_id:
    if x in id_total:
        print("Apr: " , x)
    id_total.add(x)
print("<-------May ID Duplicates----------->")
for x in may_id:
    if x in id_total:
        print("May: " , x)
    id_total.add(x)
print("<-------June ID Duplicates----------->")
for x in jun_id:
    if x in id_total:
        print("Jun: " , x)
    id_total.add(x)
print("<-------July ID Duplicates----------->")
for x in jul_id:
    if x in id_total:
        print("Jul: " , x)
    id_total.add(x)
print("<-------August ID Duplicates----------->")
for x in aug_id:
    if x in id_total:
        print("Aug: " , x)
    id_total.add(x)
print("<-------SEPTEMBER ID First Duplicates----------->")
for x in sep_first_id:
    if x in id_total:
        print("Sep First: ", x)
    id_total.add(x)

print("<-------SEPTEMBER ID Second Duplicates----------->")
for x in sep_second_id:
    if x in id_total:
        print("Sep Second : ", x)
    id_total.add(x)

print("<-------SEPTEMBER ID Third Duplicates----------->")
for x in sep_third_id:
    if x in id_total:
        print("Sep Third: ", x)
    id_total.add(x)

print("<-------SEPTEMBER ID Fourth Duplicates----------->")
for x in sep_fourth_id:
    if x in id_total:
        print("Sep Fourth: ", x)
    id_total.add(x)




all = (len(october) + len(nov) + len(dec) + len(jan) + len(feb) + len(mar) + len(apr) + len(may) + len(may) + len(jul) + len(aug) + len(sep_first) + len(sep_second) + len(sep_third) + len(sep_fourth)) 
print('<---------------- All events  Total pulled before added to set----------------------->')
print(all)

print('<---------------- Total events after dups removed using set----------------------->')
print(len(total))

each_month = (f' OCT: {len(october)}\n Nov: {len(nov)}\n Dec: {len(dec)}\n Jan: {len(jan)}\n Feb: {len(feb)}\n Mar: {len(mar)} \n Apr: {len(apr)}\n May: {len(may)}\n Jun: {len(jun)}\n Jul: {len(jul)}\n Aug: {len(aug)}\n Sep first: {len(sep_first)}\n Sep Second: {len(sep_second)}\n Sep Third: {len(sep_third)}\n Sep Fourth: {len(sep_fourth)}\n')
print('<---------------- Each Month total----------------------->')
print(each_month)

ids = (f' OCT: {len(october_id)}\n Nov: {len(nov_id)}\n Dec: {len(dec_id)}\n Jan: {len(jan_id)}\n Feb: {len(feb_id)}\n Mar: {len(mar_id)} \n Apr: {len(apr_id)}\n May: {len(may_id)}\n Jun: {len(jun_id)}\n Jul: {len(jul_id)}\n Aug: {len(aug_id)}\n Sep First: {len(sep_first_id)}\n Sep Second: {len(sep_second_id)}\n Sep Third: {len(sep_third_id)}\n Sep Fourth: {len(sep_fourth_id)}\n')
print('<---------------- IDS by Month------------------->')
print(ids)

print('<---------------- Total IDs after dups removed using set----------------------->')
print(len(id_total))


#*  RESULTS

'''
The Duplicates occur because some events have a date range and some hit both date URL's because of this. Using Set to eliminate Duplicates within date ranges
'''

# <-------October Duplicates----------->
# <-------November Duplicates----------->
# Nov:  https://10times.com/hbpsurg
# Nov:  https://10times.com/wine-spirits-summit
# Nov:  https://10times.com/devfesttoulouse
# Nov:  https://10times.com/idcreatives-clermont-ferrand
# Nov:  https://10times.com/salon-dela-photo
# <-------December Duplicates----------->
# Dec:  https://10times.com/antiques-fair-nimes
# Dec:  https://10times.com/festival-lights
# Dec:  https://10times.com/biennale
# <-------January Duplicates----------->
# <-------February Duplicates----------->
# Feb:  https://10times.com/paris-student-fair
# Feb:  https://10times.com/cam-therapies
# Feb:  https://10times.com/icc-international-mediation
# <-------March Duplicates----------->
# Mar:  https://10times.com/agricultural-show
# Mar:  https://10times.com/tranoi-preview
# <-------April Duplicates----------->
# <-------May Duplicates----------->
# May:  https://10times.com/ceva
# May:  https://10times.com/e13s-zxp1-xs03
# May:  https://10times.com/carrefour-des-gestions-locales-de-leau
# May:  https://10times.com/rdd-nice
# May:  https://10times.com/weurman-flavour-research-symposium-dijon
# <-------June Duplicates----------->
# Jun:  https://10times.com/salon-habitat-deco
# Jun:  https://10times.com/salon-vivre-cotesud
# Jun:  https://10times.com/international-symposium-on-auriculotherapy
# Jun:  https://10times.com/foires-de-champagne
# Jun:  https://10times.com/foire-exposition-dangers2015
# Jun:  https://10times.com/habitat-immobilier-nature-et-decoration
# <-------July Duplicates----------->
# Jul:  https://10times.com/isos-toulouse
# Jul:  https://10times.com/apparel-sourcing-paris
# Jul:  https://10times.com/e1z4-f9r3-k0pf
# Jul:  https://10times.com/bistops
# Jul:  https://10times.com/iaee-paris
# Jul:  https://10times.com/compas-lyon
# Jul:  https://10times.com/e1sx-3922-fsxf
# Jul:  https://10times.com/esat-paris
# Jul:  https://10times.com/avantex-paris
# Jul:  https://10times.com/ijcar-aubervilliers
# Jul:  https://10times.com/mice-place-marseille
# <-------August Duplicates----------->
# <-------SEPTEMBER First Duplicates----------->
# Sep First:  https://10times.com/hyp-conference-lyon
# Sep First:  https://10times.com/art-o-rama
# Sep First:  https://10times.com/salon-des-vins-et-de-la-gastronomie-de-biarritz
# Sep First:  https://10times.com/e14z-zzr9-gg47
# Sep First:  https://10times.com/international-foire-europeenne
# Sep First:  https://10times.com/world-conservation-congress-marseille
# <-------SEPTEMBER Second Duplicates----------->
# Sep Second :  https://10times.com/ecoc-exhibition-bordeaux
# Sep Second :  https://10times.com/salon-national
# Sep Second :  https://10times.com/national-exhibition-shellfish-and-marine-cultures
# Sep Second :  https://10times.com/international-conference-on-neurology-neuro-disord
# Sep Second :  https://10times.com/salonsce-lyon
# Sep Second :  https://10times.com/medfit-conference-grenoble
# Sep Second :  https://10times.com/space-expo-rennes
# Sep Second :  https://10times.com/e1zf-32rz-1rh1
# Sep Second :  https://10times.com/e1zf-50h1-8dkr
# Sep Second :  https://10times.com/e1zp-10px-01zs
# Sep Second :  https://10times.com/imog-montpellier
# Sep Second :  https://10times.com/salonsce-montpellier
# Sep Second :  https://10times.com/simesitem-expo-paris
# Sep Second :  https://10times.com/fair-of-savoie
# Sep Second :  https://10times.com/surgery-and-anaesthesia-paris
# Sep Second :  https://10times.com/immunorad
# <-------SEPTEMBER Third Duplicates----------->
# Sep Third:  https://10times.com/cartoon-forum
# Sep Third:  https://10times.com/e11z-g8fs-5dg1
# Sep Third:  https://10times.com/iopc
# Sep Third:  https://10times.com/e1s4-7k37-kggh
# Sep Third:  https://10times.com/equipbaie-paris
# Sep Third:  https://10times.com/e1z2-8d0h-5zkh
# Sep Third:  https://10times.com/chimielyon
# Sep Third:  https://10times.com/e13z-pp5f-kf24
# Sep Third:  https://10times.com/european-dysmorphology-meeting
# Sep Third:  https://10times.com/seanergy-forum
# Sep Third:  https://10times.com/e1sk-d055-g5fp
# Sep Third:  https://10times.com/copd-paris
# Sep Third:  https://10times.com/geopolitics-and-economics-iot-ai-and-robotics
# Sep Third:  https://10times.com/world-congress-on-nursing-and-healthcare-paris
# Sep Third:  https://10times.com/e1zf-hzz3-41s7
# Sep Third:  https://10times.com/netgcoop-carg-se
# Sep Third:  https://10times.com/e1zs-43fg-59dp
# Sep Third:  https://10times.com/e1z3-0d0h-z3ks
# Sep Third:  https://10times.com/sfm-nantes
# Sep Third:  https://10times.com/e1s3-k7k0-z6pd
# Sep Third:  https://10times.com/e1zp-k06r-z3r1
# Sep Third:  https://10times.com/taste-paris-france
# Sep Third:  https://10times.com/professional-showroom-dedicated-to-internet
# Sep Third:  https://10times.com/industrial-analysis-exhibition
# Sep Third:  https://10times.com/decielec-t
# Sep Third:  https://10times.com/e1zp-502k-z8dk
# Sep Third:  https://10times.com/e1s5-r4r0-g0rs
# Sep Third:  https://10times.com/e14z-fhz9-rf08
# Sep Third:  https://10times.com/le-cuir-a-paris
# Sep Third:  https://10times.com/foire-de-pau
# Sep Third:  https://10times.com/e1z5-g5f1-g9pd
# <-------SEPTEMBER Fourth Duplicates----------->
# Sep Fourth:  https://10times.com/salonsce-paris
# Sep Fourth:  https://10times.com/isga-nancy
# Sep Fourth:  https://10times.com/vannes-fair
# Sep Fourth:  https://10times.com/leisure-vehicles-trade-show
# Sep Fourth:  https://10times.com/gpmb-paris
# Sep Fourth:  https://10times.com/preventica-north-france
# Sep Fourth:  https://10times.com/e1z1-h9p3-h2sh
# Sep Fourth:  https://10times.com/e10z-pxd3-ff29
# Sep Fourth:  https://10times.com/e1z2-41z4-rhpp
# Sep Fourth:  https://10times.com/e1s1-x8z0-p8gh
# Sep Fourth:  https://10times.com/e1z3-854h-rzrk
# Sep Fourth:  https://10times.com/brains-paris
# Sep Fourth:  https://10times.com/international-metrology-congress
# Sep Fourth:  https://10times.com/e1z0-34r7-pdpk
# Sep Fourth:  https://10times.com/it-partners
# Sep Fourth:  https://10times.com/e1zp-30xf-1r3g
# Sep Fourth:  https://10times.com/sfen-npc
# Sep Fourth:  https://10times.com/pour-lamour-du
# Sep Fourth:  https://10times.com/batteries-event-lyon
# Sep Fourth:  https://10times.com/e1s4-x2pz-5f8p
# Sep Fourth:  https://10times.com/international-meeting-on-ampk-vian-les-bains
# Sep Fourth:  https://10times.com/grand-pavois-rochelle
# Sep Fourth:  https://10times.com/e1z5-2s0f-6rrk
# Sep Fourth:  https://10times.com/e1sx-s14f-s5g9
# Sep Fourth:  https://10times.com/salon-alina-bordeaux
# Sep Fourth:  https://10times.com/foireinternationale-saint-etienne
# Sep Fourth:  https://10times.com/foire-internationale-de-metz
# Sep Fourth:  https://10times.com/devoxx-france
# Sep Fourth:  https://10times.com/ai-net-conference
# Sep Fourth:  https://10times.com/measurement-world-france
# Sep Fourth:  https://10times.com/mobilehci-toulouse
# Sep Fourth:  https://10times.com/equipmag-expo
# <-------October ID Duplicates----------->
# <-------November ID Duplicates----------->
# Nov:  48676
# Nov:  385122
# Nov:  431147
# Nov:  447438
# Nov:  2849
# <-------December ID Duplicates----------->
# Dec:  452788
# Dec:  247967
# Dec:  75885
# <-------January ID Duplicates----------->
# <-------February ID Duplicates----------->
# Feb:  462736
# Feb:  100963
# Feb:  343135
# <-------March ID Duplicates----------->
# Mar:  15412
# Mar:  71705
# <-------April ID Duplicates----------->
# <-------May ID Duplicates----------->
# May:  160846
# May:  114783
# May:  569495
# May:  475521
# May:  360826
# <-------June ID Duplicates----------->
# Jun:  199082
# Jun:  179557
# Jun:  57993
# Jun:  320363
# Jun:  410380
# Jun:  145367
# <-------July ID Duplicates----------->
# Jul:  483891
# Jul:  312725
# Jul:  420887
# Jul:  607840
# Jul:  30195
# Jul:  376315
# Jul:  472012
# Jul:  590590
# Jul:  484485
# Jul:  454500
# Jul:  412000
# <-------August ID Duplicates----------->
# <-------SEPTEMBER ID First Duplicates----------->
# Sep First:  169276
# Sep First:  666733
# Sep First:  48771
# Sep First:  370146
# Sep First:  481203
# Sep First:  101563
# <-------SEPTEMBER ID Second Duplicates----------->
# Sep Second :  446278
# Sep Second :  18168
# Sep Second :  145471
# Sep Second :  434625
# Sep Second :  52705
# Sep Second :  426293
# Sep Second :  607672
# Sep Second :  602187
# Sep Second :  44339
# Sep Second :  468961
# Sep Second :  424445
# Sep Second :  455173
# Sep Second :  42036
# Sep Second :  21435
# Sep Second :  644965
# Sep Second :  340583
# <-------SEPTEMBER ID Third Duplicates----------->
# Sep Third:  465165
# Sep Third:  133669
# Sep Third:  128062
# Sep Third:  18230
# Sep Third:  577375
# Sep Third:  630341
# Sep Third:  163254
# Sep Third:  398577
# Sep Third:  435986
# Sep Third:  630513
# Sep Third:  278748
# Sep Third:  588332
# Sep Third:  648618
# Sep Third:  515267
# Sep Third:  602670
# Sep Third:  644080
# Sep Third:  612685
# Sep Third:  588641
# Sep Third:  648767
# Sep Third:  485097
# Sep Third:  392543
# Sep Third:  612682
# Sep Third:  581304
# Sep Third:  319833
# Sep Third:  602665
# Sep Third:  264129
# Sep Third:  474770
# Sep Third:  341298
# Sep Third:  5175
# Sep Third:  444929
# Sep Third:  650314
# <-------SEPTEMBER ID Fourth Duplicates----------->
# Sep Fourth:  461015
# Sep Fourth:  649073
# Sep Fourth:  649100
# Sep Fourth:  453893
# Sep Fourth:  445589
# Sep Fourth:  23393
# Sep Fourth:  427301
# Sep Fourth:  5834
# Sep Fourth:  483984
# Sep Fourth:  469818
# Sep Fourth:  226487
# Sep Fourth:  594604
# Sep Fourth:  454875
# Sep Fourth:  379419
# Sep Fourth:  55862
# Sep Fourth:  486888
# Sep Fourth:  145460
# Sep Fourth:  627678
# Sep Fourth:  18173
# Sep Fourth:  7727
# Sep Fourth:  650778
# Sep Fourth:  674148
# Sep Fourth:  75913
# Sep Fourth:  64476
# Sep Fourth:  595053
# Sep Fourth:  384062
# Sep Fourth:  596432
# Sep Fourth:  624252
# Sep Fourth:  667244
# Sep Fourth:  8722
# Sep Fourth:  383426
# Sep Fourth:  379754
# <---------------- All events  Total pulled before added to set----------------------->
# 942
# <---------------- Total events after dups removed using set----------------------->
# 840
# <---------------- Each Month total----------------------->
#  OCT: 115
#  Nov: 89
#  Dec: 26
#  Jan: 34
#  Feb: 21
#  Mar: 44 
#  Apr: 38
#  May: 64
#  Jun: 82
#  Jul: 47
#  Aug: 41
#  Sep first: 62
#  Sep Second: 84
#  Sep Third: 106
#  Sep Fourth: 107

# <---------------- IDS by Month------------------->
#  OCT: 115
#  Nov: 89
#  Dec: 26
#  Jan: 34
#  Feb: 21
#  Mar: 44 
#  Apr: 38
#  May: 64
#  Jun: 82
#  Jul: 47
#  Aug: 41
#  Sep First: 62
#  Sep Second: 84
#  Sep Third: 106
#  Sep Fourth: 107

# <---------------- Total IDs after dups removed using set----------------------->
# 840


