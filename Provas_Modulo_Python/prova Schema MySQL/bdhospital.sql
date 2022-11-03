CREATE DATABASE IF NOT EXISTS HOSPITAL;
USE HOSPITAL;

CREATE TABLE IF NOT EXISTS PACIENTES(
										matricula INTEGER PRIMARY KEY AUTO_INCREMENT,
                                        nome VARCHAR(40) NOT NULL,
                                        idade INT 
                                        );

CREATE TABLE IF NOT EXISTS MEDICOS(
										CRM INTEGER PRIMARY KEY AUTO_INCREMENT,
                                        mnome VARCHAR(40) NOT NULL,
                                        ALA VARCHAR (40)
                                    );

CREATE TABLE IF NOT EXISTS CONSULTA (
										PACIENTES_matricula INTEGER,
                                        MEDICOS_CRM INTEGER,
                                        PRIMARY KEY(PACIENTES_matricula,MEDICOS_CRM),
                                        FOREIGN KEY (PACIENTES_matricula) REFERENCES PACIENTES(matricula)
										);

INSERT INTO PACIENTES(nome,idade)VALUES("MIKE O MIKE", 26);
INSERT INTO PACIENTES(nome,idade)VALUES("JULIOS O JULIOS", 40);
INSERT INTO PACIENTES(nome,idade)VALUES("CRIS O CRIS", 26);

INSERT INTO MEDICOS(mnome,ALA)VALUES("DR.LA-MUERTE","HUROLOGIA");
INSERT INTO MEDICOS(mnome,ALA)VALUES("DR.VIVERÁ","CARDIOLOGISTA");
SELECT PACIENTES.nome, PACIENTES.idade, MEDICOS.mnome,MEDICOS.ALA FROM PACIENTES,MEDICOS;
