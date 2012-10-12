 # -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from django.core.management import setup_environ
import settings
setup_environ(settings)

from co2r.main.models import Locale

data = {'co2r': "CO2R",
    'shoot': "Shoot",
    'our_mission': "Our mission",
    'faq': "FAQ",
    'register_your_product': "Register your product",
    'other_things_you_can_do': "Other things you can do to help",
    'give_us_feedback': "Give us feedback",
    'feedback_message_prompt': "Idea? Complaint? Praise? Question?",
    'learn_more_about_co2r': "Learn more about the CO2R platform",
    'learn_more': "Learn More",
    'trees_planted': "%s Trees planted",
    'email': "Email",
    'phone': "Phone",
    'inquire': "Inquire",
    'name_or_organization': "Name/Organization",
    'your_message': "Your message",
    'register_introduction': "Contact us about your product or just drop us a line. We're interested in hearing from you whether your're an experienced green company or just venturing out. We can answer your questions and get you going.",
    'introduction_title': "CO<sub>2</sub> Responsible",
    'introduction_text': '<p class="lead">We help companies be responsble about the <span co2r-definition>carbon</span> their products emit into the atmosphere. We achieve this by planting enough trees in Nicaragua to negate their emissions. </p> <p>Sed ut perspiciatis unde omnis iste natus error [Taking Root] sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo.</p>',
    'directory_filter_input_prompt': 'Filter CO2 responsible products by name',
    'can_do_feedback_title': "Give us feedback",
    'can_do_feedback_description': "<p>lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>",
    'can_do_spread_word_title': "Spread the word",
    'can_do_spread_word_description': "<p>lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>",
    'can_do_recruit_company_title': "Recruit a company",
    'can_do_recruit_company_description': "<p>lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>",
    'can_do_sponsor_co2r_title': "Sponsor us",
    'can_do_sponsor_co2r_description': "<p>lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>",
    'artifact_download_report': "Download the %s report",
    'artifact_business_card_contact_lead_in': "Get in touch:",
    'artifact_offset_since': "Offset since %s",
    'artifact_reports_section_title': "Footprint Summary Reports",
    'artifact_other_eco_actions': 'Other environmental actions',
    'artifact_total_vs_offset': 'Total <span class="co2-keyword">CO<sub>2</sub></span> produced and total <span class="co2-keyword">CO<sub>2</sub></span> offset',
    'artifact_co2_sources': '%s sources',
    'artifact_co2_per_thing_made': '%s for %s',
    'about_tab_label_map': "Map",
    'about_tab_label_video': "Video",
    'about_topic_1_title': "Ecosystems",
    'about_topic_1_text': '<p class="lead"> One of the three main aims of Taking Root\'s project is to protect and restore ecosystems through reforestation. Here are some of the ways this is done.</p>, <h5>Preserving ecosystems</h5>, <p> Forest preservation: In order to protect other forests from being cut down for farmland, Taking Root only reforests land that isn\'t being used. Also, specific trees are planted for the farmers to use as firewood and timber.</p> <p> Air quality: Trees improve air quality by retaining humidity, absorbing carbon and producing oxygen.</p> <p> Waterways: The trees help capture water in the dry season and minimize flooding and landslides in the rainy season. They also help regulate the water that flows into the nearby Estero Real, one of Central America\'s most important estuaries in terms of biodiversity.</p>',
    'about_topic_2_title': "Livelihoods",
    'about_topic_2_text': '<p class="lead"> A second core aim of the project is to improve the livelihoods of the participating community members through reforestation.</p> <h5> Improving livelihoods</h5> <p> With over 136 small-scale farmers in 21 communities as of 2012 working to reforest underutilized parts of their land, there are a lot of people involved in every step of the process. Among other things, participants help select the tree species, gather seeds, build nurseries, plant trees, and protect them as they grow.</p> <p> Incentives are put into place to encourage participation and help farmers at each step of the project.</p> <p> Interest-free loans: Taking Root provides interest-free loans to help farmers build fencing, clear shrubs and plant the seedlings. This in turn generates many jobs within the community.</p>',
    'about_topic_3_title': "Climate Change",
    'about_topic_3_text': '<p class="lead">The third core aim of the project is to use social reforestation to tackle climate change, a serious global issue that must be addressed.</p> <h5>Mitigating climate change</h5> <p>Preventing emissions: Deforestation accounts for over 17% of global CO2 emissions - almost as much as all the cars, trucks, boats and planes on the planet combined! By working with communities to preserve forests and prevent further destruction, Taking Root is reducing the amount of CO2 released into the atmosphere.</p> <p>Effective carbon pumps: Since about half of a tree\'s dry weight is made of carbon, trees serves as pumps, pulling CO2 out of the air and storing it in their plant tissue. Closer to the equator, these trees can grow up to 10 times faster than in northern climates.</p>',
    'about_community_title': "The Limay Community Carbon Project",
    'about_community_text': '<p> The Limay Community Carbon Project is a community-based reforestation initiative that works with small-scale farming families in Nicaragua to restore ecosystems, improve livelihoods and tackle climate change.</p> <p> The project is developed according to the [Plan Vivo Standard], a system that offers incentives to farmers who agree to manage their land in a way that provides an ecological service, such as planting and maintaining trees to absorb carbon.</p> <p> The Limay Community Carbon Project is developed by [Taking Root], a non-profit organization, based in Montreal (Canada).</p>',
    'footer_sponsor_name': "Caisse d'economie solidaire",
    'footer_sponsor_description': "Réalisé avec la participation financière de la Caisse d’économie solidaire Desjardins, qui contribue à bâtir un Québec plus juste dans la perspective d’un développement durable.",
    'footer_sponsor_link': "http://www.caissesolidaire.coop",
    'footer_taking_root': "Taking root",
    'footer_taking_root_description': "lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et doloremn.",
    'footer_colofon': 'Colofon: Site design and frontend development by <a href="http://www.jaosnkuhrt.com">Jason kuhrt</a>. API and backend development by <a> Pierre Drescher</a>. Tools used: <a href="http://angularjs.org">Angularjs</a>, <a href="http://meteor.com">Meteor</a>, <a href="http://meteor.com">Django</a>. <a href="http://Heroku.com">Heroku</a>.'
    }

try:
    en = Locale.objects.get(language ='en')
except Locale.DoesNotExist:
    en = Locale(language ='en')

for key, value in data.iteritems():
    setattr(en, key, value)

en.save()

fr, created = Locale.objects.get_or_create(language='fr')

