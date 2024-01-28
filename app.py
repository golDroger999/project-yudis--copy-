import streamlit as st
from docxtpl import DocxTemplate
st.set_page_config (layout="wide")

doc = DocxTemplate("template/template.docx")
def generate_word_document(drive_model, 
                           drive_serial_number, 
                           source_data_size,
                           sector_count,
                           md5_checksum,
                           sha5_checksum,
                           jumlah_temuan,
                           jenis_temuan,
                           status_drive_model,
                           status_drive_serial_number,
                           status_source_data_size,
                           status_sector_count,
                           status_md5_checksum,
                           status_sha5_checksum,
                           status_jumlah_temuan,
                           status_jenis_temuan):
    context ={
        'drive_model': drive_model,
        'drive_serial_number':drive_serial_number,
        'source_data_size':source_data_size,
        'sector_count':sector_count,
        'md5_checksum':md5_checksum,
        'sha5_checksum':sha5_checksum,
        'jumlah_temuan': jumlah_temuan,
        'jenis_temuan':jenis_temuan,

        'status_drive_model': status_drive_model,
        'status_drive_serial_number': status_drive_serial_number,
        'status_source_data_size': status_source_data_size,
        'status_sector_count' : status_sector_count,
        'status_md5_checksum' : status_md5_checksum,
        'status_sha5_checksum' :status_sha5_checksum,
        'status_jumlah_temuan': status_jumlah_temuan,
        'status_jenis_temuan': status_jenis_temuan
    }
    doc.render(context=context)
    doc.save('generate.docx')

def main():
    st.subheader("PROJECT YUDIS")
    colname, coldate= st.columns(2)
    with colname:
        nama_form = st.text_input('Document Name')
        
    with coldate:
        date_form = st.date_input('Date Input')
    
    note_form = st.text_area('Note')
    
    st.write('.')
    col1,col2 = st.columns(2) 
    with col1:
        with st.expander('FORM INPUT'):
            drive_model = st.text_input("Drive Model")
            drive_serial_number = st.text_input("Drive Serial Number")
            source_data_size = st.text_input("Source Data Size")
            sector_count = st.text_input("Sector count")
            md5_checksum = st.text_input("MD5 Checksum")
            sha5_checksum = st.text_input("SHA5 Checksum")
            jumlah_temuan = st.text_input("Jumlah Temuan")
            jenis_temuan = st.text_input("Jenis Temuan")
            
        # with col3:
        #     st.write('')
        
        
    with col2:
        with st.expander('status'):
            status_drive_model = st.selectbox("Status Drive Model", ('verified', "match"))
            status_drive_serial_number = st.selectbox("Status Drive Serial Number", ('verified', "match"))
            status_source_data_size = st.selectbox("Status Source Data Size", ('verified', "match"))
            status_sector_count = st.selectbox("Status Sector count", ('verified', "match"))
            status_md5_checksum = st.selectbox("Status MD5 Checksum", ('verified', "match"))
            status_sha5_checksum = st.selectbox("Status SHA5 Checksum", ('verified', "match"))
            status_jumlah_temuan = st.selectbox("Status Jumlah Temuan", ('verified', "match"))
            status_jenis_temuan = st.selectbox("Status Jenis Temuan", ('verified', "match"))  
    st.write('.')         
    if st.button('buat laporan'):
        generate_word_document(drive_model, drive_serial_number,  source_data_size, sector_count,
                           md5_checksum, sha5_checksum, jumlah_temuan, jenis_temuan, status_drive_model, status_drive_serial_number,
                           status_source_data_size, status_sector_count, status_md5_checksum, status_sha5_checksum, status_jumlah_temuan, status_jenis_temuan)
        
        st.write('.')
        with open('generate.docx', 'rb') as f:
            st.download_button(label='Download Generated Document',
                                data=f,
                                file_name=f'laporan.docx',
                                mime='application/vnd.openxmlformats-officedocument.wordprocessingml.document')  
            
        st.success('LAPORAN BERHASIL ')

if __name__ == "__main__":
    main()
