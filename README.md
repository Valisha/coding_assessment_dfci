# Coding test of Bioinformatics Software Engineer
### Author: Valisha Shah
### Date: 03/05/2024

### Task1 
#### Q1 - task1_q1.py - Python script to complete the first question in Task 1. This script will recursively find all FASTQ files in a directory and report each file name and the percent of sequences in that file that are greater than 30 nucleotides long.
##### Input: /path/to/dir
##### Command line: ./task1_q1.py /path/to/dir
##### ./task1_q1.py -h

#### Q2 - task1_q2.py - Python script to complete the second question in Task 2. This script will print out the 10 most frequent sequences from the given FASTA file, and the frequency along with the sequence
##### Input: /path/to/fasta/file
##### Command line: ./task1_q2.py /path/to/fastq/file
##### ./task1_q2.py -h

#### Q3 - task1_q3.py - Python script to complete the second question in Task 3. This script will annotate the given position and chromosome, using a GTF annotation file 
##### Input: /path/to/gtf/file
##### /path/to/coordinates
##### Command line: ./task1_q3.py /path/to/gtf/file /path/to/coordinates
##### ./task1_q3.py -h

#### Task2 - task2.py - Python script to complete Task2. This script will parse the hs_intervals file and report the mean GC coverage for the each GC_bins ##### Input: /path/to/hs_interval_file
##### Command line: ./task2.pt /path/to/hs_interval_file

#### Task3 - task3.py - Python script to complete the Task3. This script will use the given rsID to retrieve information about alleles, locations,
effects of variants in transcripts, and genes containing the transcript. 
Both python and perl script that I have made, seem to be having an HTTP error. I dont know if its just my computer or some other issue 

#### Cloud computing 

##### Q1 - 
1. Sharing Large Files (10GB to 25GB): Use a cloud storage service that supports large files such as Amazon S3, Google Cloud Storage, or Azure Blob Storage. These services are designed to handle large files and provide robust data durability.

2. Access Controls at File Level: Implement an Identity and Access Management (IAM) system.

3. Sharing Same File with Multiple Users without Making a Copy: Implement a system of pointers or references. Each user is given a pointer to the file, not a copy of the file itself. When the user requests the file, the data access layer uses the pointer to retrieve the file from cloud storage.

4. Running Bioinformatics Analysis Pipelines: Ensure the chosen cloud storage service supports the necessary integrations for running bioinformatics analysis pipelines. For example, Amazon S3 integrates well with Amazon's data analysis services.

5. Framework's Responsibility for Data Accessibility with Access Controls: Implement a data access layer that interacts with the cloud storage and IAM systems. This layer should provide an API for users to access files. When a user requests a file, the data access layer checks with the lAM system to see if the user has permission to access the file. If they do, the data access layer retrieves the file from cloud storage and sends it to the user.

##### Q2 - 
Benefits:
1. Portability: Docker ensures consistent application behavior across platforms.
2. Scalability: Kubernetes auto-scales applications based on demand.
3. Efficiency: Containers use resources more efficiently than VMs.
4. Isolation: Containers reduce dependency conflicts.
5. Reproducibility: Containers ensure consistent bioinformatics workflows.
Limitations:
1. Complexity: Kubernetes setup and management can be complex.
2. Security: Shared host OS kernel may pose security risks.
3. Storage: Persistent storage is challenging in containers.
4. Networking: Container networking can be complex.
5. Performance: Containerization may impact some HPC workloads.

##### Q3 - 

SELECT UserId, AVG(Total) AS AvgOrderTotal
FROM Invoices
GROUP BY UserId
HAVING COUNT(OrderId) >= 1;

