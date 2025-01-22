import csv

file = '' # location of your csv

for i in range(2):
    print('')

with open(file) as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

    for i, row in enumerate(spamreader):
        if i > 0:
            make = row[0]
            model = row[1]
            variation = row[2]
            
            filename = f"{make}_{model}_{variation}.py" if variation is not '' else f"{make}_{model}.py"
            filename = filename.replace(' ', '_')
            
            post_processor = row[3]
            
            unit_type = row[4]
            unit_system = 'METRIC' if unit_type == 'mm' else 'IMPERIAL'
           
            rows = [row[5], row[6], row[7]]
            working_area = tuple([float(row) for row in rows])
            
            feedrate_min = row[8]
            feedrate_max = row[9]
            feedrate_default = row[10]
            
            spindle_min = row[11]
            spindle_max = row[12]
            spindle_default = row[13]
            
            axis4 = row[14]
            axis5 = row[15]
            
            collet_size = row[16]

            preset_contents = f"""### {filename} ###
            
import bpy
d = bpy.context.scene.cam_machine
s = bpy.context.scene.unit_settings

d.post_processor = '{post_processor}'
s.system = '{unit_system}'
d.use_position_definitions = False
d.starting_position = (0.0, 0.0, 0.0)
d.mtc_position = (0.0, 0.0, 0.0)
d.ending_position = (0.0, 0.0, 0.0)
d.working_area = {working_area}
d.feedrate_min = {feedrate_min}
d.feedrate_max = {feedrate_max}
d.feedrate_default = {feedrate_default}
d.spindle_min = {spindle_min}
d.spindle_max = {spindle_max}
d.spindle_default = {spindle_default}
d.axis4 = {axis4}
d.axis5 = {axis5}
d.collet_size = {collet_size}
d.output_tool_change = True
d.output_block_numbers = False
d.output_tool_definitions = True
d.output_g43_on_tool_change = False




            """
            print(preset_contents)
